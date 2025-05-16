---
permalink: /toggle-translation
---
<html lang="{{ page.lang | default: en }}">

  {%- include head.html -%}

<body>
  {%- include header.html -%}
  <main class="page-content" aria-label="Content">
      <div class="wrapper">

  <h1>Preferences</h1>
  <ul>
  <li><a href="/toggle-translation?showTranslations=true">Turn translations on (show them)</a></li>
  <li><a href="/toggle-translation?showTranslations=false">Turn translations off (hide them)</a></li>
  </ul>

 <div class="message" id="status">Status: N/A</div>
  </div>
  </main>

<script>
  // Parse query params
  const params = new URLSearchParams(window.location.search);
  const allowedPrefs = ['showTranslations'];
  const statusEl = document.getElementById('status');

  // Helper to get cookie
  const getCookie = (name) => {
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match ? match[2] : null;
  };

  let changes = [];

  allowedPrefs.forEach(pref => {
    let value = params.get(pref);

    // If no parameter, toggle existing cookie value
    if (value === null) {
      const current = getCookie(pref);
      if (current === "true") {
        value = "false";
      } else {
        value = "true";
      }
    }

    // Set the cookie
    document.cookie = `${pref}=${value}; path=/; max-age=${60 * 60 * 24 * 30}`;
    changes.push(`${pref} = ${value}`);
  });

  // Show status
  if (changes.length > 0) {
    statusEl.textContent = `Set: ${changes.join(', ')}`;
  } else {
    statusEl.textContent = 'No preferences were set.';
  }

    // Optional redirect after delay
    // const redirectUrl = document.referrer || '/';
    // setTimeout(() => {
    //     window.location.href = redirectUrl;
    // }, 1500); // 1.5 seconds

    const redirectUrl = document.referrer || '/';
    window.location.href = redirectUrl;

</script>


    {%- include footer.html -%}
</body>
</html>
