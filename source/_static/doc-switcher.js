(function () {
  function selectedOption(select) {
    return select.options[select.selectedIndex];
  }

  function docsRootPath(pathname, currentVersion, currentLanguage) {
    const parts = pathname.split("/");
    for (let i = 0; i < parts.length - 1; i += 1) {
      if (parts[i] === currentVersion && parts[i + 1] === currentLanguage) {
        return {
          prefix: parts.slice(0, i).join("/") || "",
          suffix: parts.slice(i + 2).join("/"),
        };
      }
    }
    return {
      prefix: "",
      suffix: "",
    };
  }

  function normalizePageSuffix(suffix) {
    if (!suffix || suffix.endsWith("/")) {
      return `${suffix || ""}index.html`;
    }
    return suffix;
  }

  async function loadPagesManifest(prefix) {
    const manifestUrl = `${prefix}/docs-pages.json`;
    const response = await fetch(manifestUrl, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`failed to load ${manifestUrl}`);
    }
    return response.json();
  }

  function pageExists(manifest, version, language, pageSuffix) {
    const pages = manifest && manifest[version] && manifest[version][language];
    return Array.isArray(pages) && pages.includes(pageSuffix);
  }

  function currentThemeMode() {
    return (
      document.documentElement.dataset.mode ||
      document.documentElement.dataset.theme ||
      localStorage.getItem("mode") ||
      localStorage.getItem("theme") ||
      ""
    );
  }

  function withThemeMode(url) {
    const mode = currentThemeMode();
    if (!mode) {
      return url;
    }
    const target = new URL(url, window.location.href);
    target.searchParams.set("theme", mode);
    return target.href;
  }

  function restoreThemeMode() {
    const params = new URLSearchParams(window.location.search);
    const mode = params.get("theme");
    if (!mode) {
      return;
    }

    localStorage.setItem("mode", mode);
    localStorage.setItem("theme", mode);
    document.documentElement.dataset.mode = mode;
    document.documentElement.dataset.theme = mode;

    params.delete("theme");
    const cleanQuery = params.toString();
    const cleanUrl = `${window.location.pathname}${cleanQuery ? `?${cleanQuery}` : ""}${window.location.hash}`;
    window.history.replaceState({}, document.title, cleanUrl);
  }

  restoreThemeMode();

  async function navigateTo(version, language) {
    const announcement = document.querySelector(".mududb-announcement");
    const currentVersion = announcement ? announcement.dataset.currentVersion : "";
    const currentLanguage = announcement ? announcement.dataset.currentLanguage : "";
    if (!currentVersion || !currentLanguage || !version || !language) {
      return;
    }

    const locationParts = docsRootPath(window.location.pathname, currentVersion, currentLanguage);
    const prefix = locationParts.prefix.endsWith("/") ? locationParts.prefix.slice(0, -1) : locationParts.prefix;
    const pageSuffix = normalizePageSuffix(locationParts.suffix);
    const fallbackUrl = `${prefix}/${version}/${language}/`;
    const targetUrl = `${prefix}/${version}/${language}/${pageSuffix}`;

    try {
      const manifest = await loadPagesManifest(prefix);
      window.location.href = withThemeMode(pageExists(manifest, version, language, pageSuffix) ? targetUrl : fallbackUrl);
    } catch (error) {
      window.location.href = withThemeMode(targetUrl);
    }
  }

  function bindSwitchers() {
    document.querySelectorAll(".mududb-doc-switcher").forEach((select) => {
      select.addEventListener("change", () => {
        const option = selectedOption(select);
        if (select.dataset.switchKind === "version") {
          navigateTo(option.value, option.dataset.language);
        } else {
          navigateTo(option.dataset.version, option.value);
        }
      });
    });
  }

  function isModifiedClick(event) {
    return event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey;
  }

  function isInternalDocumentLink(link) {
    const href = link.getAttribute("href");
    if (!href || href.startsWith("#") || href.startsWith("javascript:") || href.startsWith("mailto:")) {
      return false;
    }

    const target = new URL(href, window.location.href);
    if (target.origin !== window.location.origin) {
      return false;
    }

    const pathname = target.pathname;
    return pathname.endsWith("/") || pathname.endsWith(".html");
  }

  function bindInternalLinks() {
    document.addEventListener("click", (event) => {
      if (isModifiedClick(event)) {
        return;
      }

      const link = event.target.closest("a[href]");
      if (!link || link.target || !isInternalDocumentLink(link)) {
        return;
      }

      const mode = currentThemeMode();
      if (!mode) {
        return;
      }

      event.preventDefault();
      window.location.href = withThemeMode(link.href);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      bindSwitchers();
      bindInternalLinks();
    });
  } else {
    bindSwitchers();
    bindInternalLinks();
  }
})();
