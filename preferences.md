---
layout: default
permalink: /preferences
---

<main class="page-content" aria-label="Content">
  <div class="wrapper">
    <h2>User Preferences</h2>

    <form id="prefsForm">
      <div class="form-check form-switch mb-3">
        <input class="form-check-input" type="checkbox" id="showTranslations">
        <label class="form-check-label" for="showTranslations">Show Translations</label>
      </div>
      <div class="form-check form-switch mb-3">
        <input class="form-check-input" type="checkbox" id="showHindi">
        <label class="form-check-label" for="showHindi">Show Hindi</label>
      </div>
      <div class="form-check form-switch mb-3">
        <input class="form-check-input" type="checkbox" id="allowTransliteration">
        <label class="form-check-label" for="allowTransliteration">Enable Transliteration</label>
      </div>

      <button type="submit" class="btn btn-primary">Save and go back</button>
    </form>

    <div class="message mt-3" id="status">&nbsp;</div>

    <hr>

    <h3>Bookmarks</h3>

    <div id="bookmarkSection">
      <form id="bookmarkForm" class="mb-3">
        <div class="mb-2">
          <label for="bookmarkName" class="form-label">Name the bookmark:</label>
          <input
            type="text"
            id="bookmarkName"
            class="form-control"
            placeholder="Enter a name for this bookmark"
            required
          >
        </div>
        <button type="submit" class="btn btn-success">Add Bookmark</button>
      </form>

      <ul id="bookmarkList" class="list-group"></ul>
    </div>
  </div>
</main>

<script>
  const defaultPrefs = {
    showTranslations: true,
    showHindi: true,
    allowTransliteration: false
  };

  const initPref = (id, defaultVal) => {
    const cookieVal = getCookie(id);
    const checkbox = document.getElementById(id);
    checkbox.checked = (cookieVal === null) ? defaultVal : (cookieVal === 'true');
  };

  const BOOKMARKS_KEY = 'userBookmarks';

  const getBookmarks = () => {
    try {
      return JSON.parse(localStorage.getItem(BOOKMARKS_KEY)) || [];
    } catch {
      return [];
    }
  };

  const saveBookmarks = (bookmarks) => {
    localStorage.setItem(BOOKMARKS_KEY, JSON.stringify(bookmarks));
  };

const renderBookmarks = () => {
  const list = document.getElementById('bookmarkList');
  list.innerHTML = '';

  const bookmarks = getBookmarks();

  if (bookmarks.length === 0) {
    list.innerHTML = `<li class="list-group-item">No bookmarks saved.</li>`;
    return;
  }

  bookmarks.forEach(({ name, url }, index) => {
    const li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between align-items-center flex-wrap';

    li.innerHTML = `
      <div>
        <a href="${url}" target="_blank" rel="noopener noreferrer">${name}:</a> ${url}
      </div>
      <button class="btn btn-sm btn-danger" data-index="${index}" aria-label="Remove bookmark ${name}">&times;</button>
    `;

    list.appendChild(li);
  });
};

  const removeBookmark = (index) => {
    const bookmarks = getBookmarks();
    bookmarks.splice(index, 1);
    saveBookmarks(bookmarks);
    renderBookmarks();
  };

  document.addEventListener('DOMContentLoaded', () => {
    initPref('showTranslations', defaultPrefs.showTranslations);
    initPref('showHindi', defaultPrefs.showHindi);
    initPref('allowTransliteration', defaultPrefs.allowTransliteration);

    renderBookmarks();

    // Set bookmark input placeholder with referrer URL
    const referrerUrl = document.referrer || window.location.origin;
    document.getElementById('bookmarkName').placeholder = `URL -- ${referrerUrl}`;

    document.getElementById('prefsForm').addEventListener('submit', (e) => {
      e.preventDefault();

      const prefs = ['showTranslations', 'showHindi', 'allowTransliteration'];
      prefs.forEach(pref => {
        const checked = document.getElementById(pref).checked;
        document.cookie = `${pref}=${checked}; path=/; max-age=${60 * 60 * 24 * 30}`;
      });

      document.getElementById('status').textContent = `Preferences saved. Redirecting...`;

      const ref = document.referrer;
      const redirectUrl = (ref && !ref.includes('/preferences')) ? ref : '/';
      setTimeout(() => {
        window.location.href = redirectUrl;
      }, 500);
    });

    document.getElementById('bookmarkForm').addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = document.getElementById('bookmarkName');
      const name = nameInput.value.trim();

      if (!name) return;

      const url = document.referrer || window.location.origin;

      const bookmarks = getBookmarks();
      const exists = bookmarks.some(bm => bm.url === url && bm.name === name);
      if (exists) {
        alert('This bookmark already exists.');
        return;
      }

      bookmarks.push({ name, url });
      saveBookmarks(bookmarks);
      renderBookmarks();

      nameInput.value = '';
    });

    document.getElementById('bookmarkList').addEventListener('click', (e) => {
      if (e.target.tagName === 'BUTTON') {
        const index = e.target.getAttribute('data-index');
        if (index !== null) {
          removeBookmark(Number(index));
        }
      }
    });
  });
</script>
