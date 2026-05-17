// auto-blog click tracker - 無料・無認証
// 1. アフィリエイトリンクのクリックを localStorage に記録
// 2. オプションで ntfy.sh (anonymous beacon) に通知
// 3. /click-stats.html ページで誰でも統計を閲覧可能

(function () {
  if (typeof window === "undefined") return;

  var NTFY_TOPIC = "yoton-ai-clicks-v1"; // ユニークなトピック名（誰でも見れる前提）
  var NTFY_ENABLE = true; // false にすると beacon を停止

  function trackClick(href, label) {
    try {
      var key = "auto_blog_clicks";
      var raw = localStorage.getItem(key);
      var arr = raw ? JSON.parse(raw) : [];
      var entry = {
        t: Date.now(),
        page: location.pathname,
        href: href,
        label: label || "",
      };
      arr.push(entry);
      // 最新500件のみ保持
      if (arr.length > 500) arr = arr.slice(-500);
      localStorage.setItem(key, JSON.stringify(arr));
    } catch (e) {
      // localStorage 無効環境では無視
    }

    if (NTFY_ENABLE) {
      try {
        var body = location.pathname + " -> " + (label || href.substring(0, 80));
        // navigator.sendBeacon は離脱時でも送信される
        if (navigator.sendBeacon) {
          navigator.sendBeacon("https://ntfy.sh/" + NTFY_TOPIC, body);
        }
      } catch (e) {}
    }
  }

  function isAffiliateLink(href) {
    if (!href) return false;
    return (
      href.indexOf("rakuten") >= 0 ||
      href.indexOf("amazon.co.jp") >= 0 ||
      href.indexOf("moshimo") >= 0 ||
      href.indexOf("a.r10.to") >= 0 ||
      href.indexOf("afl.rakuten") >= 0
    );
  }

  document.addEventListener("click", function (ev) {
    var el = ev.target;
    while (el && el !== document.body) {
      if (el.tagName === "A" && el.href) {
        if (isAffiliateLink(el.href)) {
          var label = (el.textContent || "").trim().substring(0, 80);
          trackClick(el.href, label);
        }
        return;
      }
      el = el.parentElement;
    }
  });

  // Expose helper for /click-stats.html page
  window.__autoBlogClicks = {
    list: function () {
      try {
        return JSON.parse(localStorage.getItem("auto_blog_clicks") || "[]");
      } catch (e) {
        return [];
      }
    },
    clear: function () {
      localStorage.removeItem("auto_blog_clicks");
    },
  };
})();
