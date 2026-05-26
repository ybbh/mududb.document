from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "source"
VERSIONS_FILE = SOURCE_ROOT / "versions" / "versions.json"
BUILD_ROOT = ROOT / "build" / "html"


def load_config() -> dict:
    with VERSIONS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def run_sphinx(version: str, language: str) -> None:
    source_dir = SOURCE_ROOT / "versions" / version / language
    if not source_dir.exists():
        raise SystemExit(f"missing documentation source: {source_dir}")

    output_dir = BUILD_ROOT / version / language
    doctree_dir = ROOT / "build" / "doctrees" / version / language

    env = os.environ.copy()
    env["MUDUDB_DOC_VERSION"] = version
    env["MUDUDB_DOC_LANGUAGE"] = language

    command = [
        sys.executable,
        "-m",
        "sphinx",
        "-b",
        "html",
        "-c",
        str(SOURCE_ROOT),
        "-d",
        str(doctree_dir),
        str(source_dir),
        str(output_dir),
    ]
    subprocess.run(command, cwd=ROOT, env=env, check=True)


def write_redirect(default_version: str, default_language: str) -> None:
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)
    target = f"{default_version}/{default_language}/"
    (BUILD_ROOT / "index.html").write_text(
        f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url={target}">
    <title>MuduDB Documentation</title>
  </head>
  <body>
    <p>Redirecting to <a href="{target}">MuduDB documentation</a>.</p>
  </body>
</html>
""",
        encoding="utf-8",
    )
    (BUILD_ROOT / ".nojekyll").write_text("", encoding="utf-8")


def write_pages_manifest(versions: list[str], languages: list[str]) -> None:
    manifest: dict[str, dict[str, list[str]]] = {}
    for version in versions:
        manifest[version] = {}
        for language in languages:
            language_root = BUILD_ROOT / version / language
            if not language_root.exists():
                continue

            pages = []
            for page in language_root.rglob("*.html"):
                relative_page = page.relative_to(language_root).as_posix()
                pages.append(relative_page)

            manifest[version][language] = sorted(pages)

    (BUILD_ROOT / "docs-pages.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build MuduDB documentation.")
    parser.add_argument("--version", help="Build only one DB documentation version.")
    parser.add_argument("--language", help="Build only one language.")
    parser.add_argument("--clean", action="store_true", help="Remove build output first.")
    args = parser.parse_args()

    config = load_config()
    versions = [args.version] if args.version else config["versions"]
    languages = [args.language] if args.language else list(config["languages"].keys())

    if args.clean and BUILD_ROOT.exists():
        shutil.rmtree(BUILD_ROOT)

    for version in versions:
        for language in languages:
            run_sphinx(version, language)

    write_pages_manifest(versions, languages)
    write_redirect(config["default_version"], config["default_language"])


if __name__ == "__main__":
    main()
