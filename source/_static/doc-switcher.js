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
      window.location.href = pageExists(manifest, version, language, pageSuffix) ? targetUrl : fallbackUrl;
    } catch (error) {
      window.location.href = targetUrl;
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

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindSwitchers);
  } else {
    bindSwitchers();
  }
})();
