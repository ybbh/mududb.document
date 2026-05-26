from __future__ import annotations

import json
import os
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERSIONS_FILE = ROOT / "versions" / "versions.json"

with VERSIONS_FILE.open("r", encoding="utf-8") as f:
    versions_config = json.load(f)

project = "MuduDB"
author = "MuduDB contributors"
copyright = "2026, MuduDB contributors"

version = os.environ.get("MUDUDB_DOC_VERSION", versions_config["default_version"])
release = version
language = os.environ.get("MUDUDB_DOC_LANGUAGE", versions_config["default_language"])


def docs_source_exists(candidate_version: str, candidate_language: str) -> bool:
    return (ROOT / "versions" / candidate_version / candidate_language / "index.md").exists()


def first_existing_language(candidate_version: str) -> str | None:
    for candidate_language in versions_config["languages"]:
        if docs_source_exists(candidate_version, candidate_language):
            return candidate_language
    return None


def version_options_html() -> str:
    options: list[str] = []
    for candidate_version in versions_config["versions"]:
        target_language = language
        if not docs_source_exists(candidate_version, target_language):
            target_language = first_existing_language(candidate_version)
        if target_language is None:
            continue
        selected = " selected" if candidate_version == version else ""
        options.append(
            "<option "
            f"value=\"{escape(candidate_version)}\" "
            f"data-language=\"{escape(target_language)}\""
            f"{selected}>"
            f"{escape(candidate_version)}"
            "</option>"
        )
    return "".join(options)


def language_options_html() -> str:
    options: list[str] = []
    for candidate_language, label in versions_config["languages"].items():
        if not docs_source_exists(version, candidate_language):
            continue
        selected = " selected" if candidate_language == language else ""
        options.append(
            "<option "
            f"value=\"{escape(candidate_language)}\" "
            f"data-version=\"{escape(version)}\""
            f"{selected}>"
            f"{escape(label)}"
            "</option>"
        )
    return "".join(options)


announcement_html = (
    f"<div class=\"mududb-announcement\" data-current-version=\"{escape(version)}\" data-current-language=\"{escape(language)}\">"
    "<span class=\"mududb-announcement-title\">MuduDB documentation</span>"
    "<label class=\"mududb-doc-switch-group\"><span class=\"mududb-doc-switch-label\">Version</span>"
    "<select class=\"mududb-doc-switcher\" data-switch-kind=\"version\">"
    f"{version_options_html()}"
    "</select>"
    "</label>"
    "<label class=\"mududb-doc-switch-group\"><span class=\"mududb-doc-switch-label\">Language</span>"
    "<select class=\"mududb-doc-switcher\" data-switch-kind=\"language\">"
    f"{language_options_html()}"
    "</select>"
    "</label>"
    "</div>"
)

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "replacements",
    "smartquotes",
    "strikethrough",
    "tasklist",
]
myst_heading_anchors = 3

html_theme = "sphinx_book_theme"
html_title = f"MuduDB {version}"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["doc-switcher.js"]
html_favicon = "_static/favicon.svg"

html_theme_options = {
    "repository_url": "https://github.com/scuptio/mududb",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": False,
    "use_download_button": False,
    "use_fullscreen_button": True,
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "navigation_with_keys": True,
    "path_to_docs": "mududb.document",
    "home_page_in_toc": True,
    "primary_sidebar_end": ["indices.html"],
    "article_header_start": [],
    "article_header_end": ["toggle-secondary-sidebar.html"],
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/scuptio/mududb",
            "icon": "fa-brands fa-github",
        },
    ],
    "announcement": announcement_html,
    "logo": {
        "text": "MuduDB",
        "image_light": "_static/mudu_logo.png",
        "image_dark": "_static/mudu_logo.png",
    },
}

html_sidebars = {
    "**": [
        "search-field.html",
        "sbt-sidebar-nav.html",
    ],
}

html_context = {
    "mududb_versions": versions_config["versions"],
    "mududb_languages": versions_config["languages"],
    "mududb_current_version": version,
    "mududb_current_language": language,
}
