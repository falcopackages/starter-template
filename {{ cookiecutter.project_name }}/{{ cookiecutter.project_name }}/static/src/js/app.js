import "../vendors/basecoat.js";
import "../vendors/dropdown-menu.js";

(function () {
  "use strict";

  const stored = localStorage.getItem("themeMode");
  const dark = stored
    ? stored === "dark"
    : matchMedia("(prefers-color-scheme: dark)").matches;
  document.documentElement.classList.toggle("dark", dark);

  const apply = (dark) => {
    document.documentElement.classList.toggle("dark", dark);
    try { localStorage.setItem("themeMode", dark ? "dark" : "light"); } catch (_) {}
  };

  document.addEventListener("basecoat:theme", (event) => {
    const mode = event.detail?.mode;
    apply(
      mode === "dark" ? true
        : mode === "light" ? false
        : !document.documentElement.classList.contains("dark")
    );
  });
})();
