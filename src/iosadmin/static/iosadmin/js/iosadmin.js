(function () {
  "use strict";

  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  ready(function () {
    document.documentElement.classList.add("iosadmin-ready");

    var header = document.getElementById("header");
    var content = document.getElementById("content-start") || document.querySelector(".content");
    if (header && content) {
      var onScroll = function () {
        header.classList.toggle("ios-scrolled", content.scrollTop > 8 || window.scrollY > 8);
      };
      content.addEventListener("scroll", onScroll, { passive: true });
      window.addEventListener("scroll", onScroll, { passive: true });
      onScroll();
    }

    document.querySelectorAll(".submit-row input, .submit-row a, .object-tools a").forEach(function (el) {
      el.addEventListener("pointerdown", function () {
        el.classList.add("ios-pressed");
      });
      ["pointerup", "pointerleave", "blur"].forEach(function (evt) {
        el.addEventListener(evt, function () {
          el.classList.remove("ios-pressed");
        });
      });
    });
  });
})();
