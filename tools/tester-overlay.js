// HW03 Task 3: watermark for cross-browser screenshots (student info + detected browser/OS + URL + time).
// Not part of the SUT under test; injected via index.html only on this local copy.
(function () {
  var STUDENT = { email: "STUDENT_EMAIL", id: "STUDENT_ID", name: "STUDENT_NAME" };
  var ua = navigator.userAgent;
  var browser = /Edg\//.test(ua) ? "Edge " + ua.match(/Edg\/([\d.]+)/)[1]
    : /Firefox\//.test(ua) ? "Firefox " + ua.match(/Firefox\/([\d.]+)/)[1]
    : /Chrome\//.test(ua) ? "Chrome " + ua.match(/Chrome\/([\d.]+)/)[1]
    : /Safari\//.test(ua) ? "Safari " + ((ua.match(/Version\/([\d.]+)/) || [])[1] || "")
    : "Unknown browser";
  var os = /Android/.test(ua) ? "Android " + ((ua.match(/Android ([\d.]+)/) || [])[1] || "")
    : /iPhone|iPad/.test(ua) ? "iOS " + ((ua.match(/OS ([\d_]+)/) || [])[1] || "").replace(/_/g, ".")
    : /Mac OS X/.test(ua) ? "macOS " + ((ua.match(/Mac OS X ([\d_.]+)/) || [])[1] || "").replace(/_/g, ".")
    : /Windows NT 10/.test(ua) ? "Windows 10/11" : navigator.platform;
  function render() {
    var el = document.getElementById("hw03-overlay") || document.createElement("div");
    el.id = "hw03-overlay";
    el.setAttribute("aria-hidden", "true");
    el.style.cssText = "position:fixed;right:8px;bottom:8px;z-index:2147483647;pointer-events:none;" +
      "background:rgba(0,0,0,.78);color:#fff;font:12px/1.4 Arial,sans-serif;padding:6px 10px;border-radius:6px;max-width:92vw";
    el.textContent = STUDENT.email + " | " + STUDENT.id + " | " + STUDENT.name + " | " + browser + " / " + os +
      " | " + location.href + " | " + new Date().toLocaleString("vi-VN");
    if (!el.parentNode) document.body.appendChild(el);
  }
  if (document.body) render(); else document.addEventListener("DOMContentLoaded", render);
  setInterval(render, 1000);
})();
