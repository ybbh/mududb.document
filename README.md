# MuduDB Documentation

This repository contains the Sphinx documentation project for MuduDB.

The documentation is written in Markdown through MyST Parser, organized by database version and language, and built into static HTML for publication.

## Layout

```text
mududb.document/
  source/
    conf.py
    _static/
      custom.css
    versions/
      v0.1/
        en/
          index.md
          ...
        zh_CN/
          index.md
          ...
  scripts/
    build_docs.py
  .github/
    workflows/
      docs.yml
```

Version and language are both part of the source path:

```text
source/versions/<db-version>/<language>/
```

Current starter content:

- `v0.1/en`
- `v0.1/zh_CN`

Add future database versions by copying an existing version directory, for example:

```powershell
Copy-Item -Recurse source\versions\v0.1 source\versions\v0.2
```

Then update `source/versions/versions.json`.

## Requirements

Use Python 3.10 or newer.

```bash
python -m pip install -r requirements.txt
```

## Build

Build all configured versions and languages:

```bash
python scripts/build_docs.py
```

Build one version and language:

```bash
python scripts/build_docs.py --version v0.1 --language en
python scripts/build_docs.py --version v0.1 --language zh_CN
```

Generated HTML is written to:

```text
build/html/<version>/<language>/
```

The script also creates:

- `build/html/index.html`, redirecting to the default version and language.
- `build/html/.nojekyll`, for GitHub Pages compatibility.

## Local Preview

After building:

```bash
python -m http.server 8000 --directory build/html
```

Open:

```text
http://127.0.0.1:8000/
```

## Writing Guide

Write pages in Markdown (`.md`). MyST extensions are enabled for common documentation features:

- fenced code blocks
- tables
- definition lists
- task lists
- admonitions
- colon fences
- field lists
- smart quotes and replacements

Use Sphinx toctrees in Markdown:

````md
```{toctree}
:maxdepth: 2

getting-started/index
reference/index
```
````

Each page should belong to one version and one language. Do not share mutable text files across languages; keep translation ownership explicit.

## Version Maintenance

Use this policy for database releases:

- Patch-level documentation fixes can be made in the affected version directory.
- New feature documentation should be added to the next active version directory.
- When a DB release becomes historical, keep its directory intact and avoid restructuring it.
- If a page is removed in a future version, leave the older version unchanged.

Update `source/versions/versions.json` when adding or retiring maintained versions:

```json
{
  "default_version": "v0.1",
  "default_language": "zh_CN",
  "versions": ["v0.1"],
  "languages": {
    "en": "English",
    "zh_CN": "简体中文"
  }
}
```

## Publication Workflow

The workflow at `.github/workflows/docs.yml` builds the final static HTML and publishes only generated artifacts.

The workflow publishes generated HTML to `https://github.com/mududb/docs`.

Configure these repository variables/secrets in the documentation repository:

- Secret `PAGES_DEPLOY_TOKEN`: GitHub token with write access to `mududb/docs`.

The workflow publishes `build/html` into the root of `mududb/docs`. Source files from this repository are not published.
Publishing is manual: run the workflow with `command=publish`. Pushes to `main` run the build job only.

## Manual Release Checklist

1. Update or copy the version directory under `source/versions`.
2. Update `source/versions/versions.json`.
3. Build locally with `python scripts/build_docs.py`.
4. Inspect `build/html/index.html` and one language page.
5. Push to `main`; the workflow builds and deploys the generated HTML.
