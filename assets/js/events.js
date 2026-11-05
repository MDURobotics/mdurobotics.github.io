// Moves events whose end time has passed from the upcoming list(s) to the
// past list, in Swedish local time. Without JS the build-time split is shown.
(function () {
  var fmt = new Intl.DateTimeFormat("sv-SE", {
    timeZone: "Europe/Stockholm", year: "numeric", month: "2-digit",
    day: "2-digit", hour: "2-digit", minute: "2-digit", hour12: false
  });

  // "2026-11-05 14:03" in Stockholm time; compares correctly as a string
  function now() {
    var p = {};
    fmt.formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
    return p.year + "-" + p.month + "-" + p.day + " " + (p.hour === "24" ? "00" : p.hour) + ":" + p.minute;
  }

  // End of the event: the last clock time in "time" ("10:00–11:00" -> 11:00),
  // or the end of the day when no time is given
  function end(li) {
    var times = (li.dataset.time || "").match(/\d{1,2}[:.]\d{2}/g);
    var t = times ? times[times.length - 1].replace(".", ":") : "23:59";
    if (t.length === 4) t = "0" + t;
    return li.dataset.date + " " + t;
  }

  function update() {
    var n = now();
    var past = document.querySelector('ul[data-events="past"]');
    document.querySelectorAll('ul[data-events="upcoming"]').forEach(function (ul) {
      Array.prototype.slice.call(ul.children).forEach(function (li) {
        if (end(li) > n) return;
        if (!past) { li.remove(); return; }
        // past list is newest first
        var before = Array.prototype.find.call(past.children, function (o) {
          return o.dataset.date < li.dataset.date;
        });
        li.hidden = false;
        past.insertBefore(li, before || null);
      });
      var limit = parseInt(ul.dataset.limit, 10);
      if (limit) Array.prototype.forEach.call(ul.children, function (li, i) { li.hidden = i >= limit; });
    });
    document.querySelectorAll("p[data-events-empty]").forEach(function (p) {
      var ul = document.querySelector('ul[data-events="' + p.dataset.eventsEmpty + '"]');
      p.hidden = !!(ul && ul.children.length);
    });
  }

  update();
  setInterval(update, 60 * 1000);
})();
