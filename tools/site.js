// One page at a time, chosen by the address's plain #name. An unknown name shows the summary.
(function () {
  var pages = {};
  document.querySelectorAll('section[data-page]').forEach(function (s) {
    pages[s.dataset.page] = s;
  });
  function show() {
    var name = decodeURIComponent(location.hash.slice(1));
    var page = pages[name] || pages.summary;
    Object.keys(pages).forEach(function (k) {
      pages[k].hidden = pages[k] !== page;
    });
    var parent = page.dataset.parent === 'nav' ? page.dataset.page : page.dataset.parent;
    document.querySelectorAll('[data-nav]').forEach(function (a) {
      if (a.dataset.nav === parent) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
    window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', show);
  show();

  var filter = document.getElementById('game-filter');
  if (filter) {
    filter.addEventListener('input', function () {
      var q = filter.value.trim().toLowerCase();
      document.querySelectorAll('table.filterable tbody tr').forEach(function (row) {
        row.hidden = q !== '' && row.textContent.toLowerCase().indexOf(q) === -1;
      });
    });
  }
})();
