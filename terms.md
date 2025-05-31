---
layout: default
permalink: /terms
---

{% assign term_docs = "" | split: "" %}

{% for doc in site.tb_question %}
  {% if doc.index_terms %}
    {% for term in doc.index_terms %}
      {% assign record = term | append: "||" | append: "तत्त्वबोधे -- " | append: doc.question_text_skt | append: "||" | append: doc.url %}
      {% assign term_docs = term_docs | push: record %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% for doc in site.avarta %}
  {% if doc.index_terms %}
    {% for term in doc.index_terms %}
      {% assign record = term | append: "||" | append: "विचारसागरे " | append: doc.title | append: "||" | append: doc.url %}
      {% assign term_docs = term_docs | push: record %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% for doc in site.chandra_question %}
  {% if doc.index_terms %}
    {% for term in doc.index_terms %}
      {% assign record = term | append: "||" | append: "विचारचन्द्रोदये " | append: doc.kala_number | append: "." | append: doc.question_number | append: " -- " | append: doc.question_text_skt | default: glossary_name | append: "||" | append: doc.url %}
      
      {% assign term_docs = term_docs | push: record %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% for doc in site.upanishads %}
  {% if doc.index_terms %}
    {% for term in doc.index_terms %}
      {% assign record = term | append: "||" | append: doc.title | append: "||" | append: doc.url %}
      {% assign term_docs = term_docs | push: record %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% for doc in site.essays %}
  {% if doc.index_terms %}
    {% for term in doc.index_terms %}
      {% assign record = term | append: "||" | append: "लेखः -- " | append: doc.title | append: "||" | append: doc.url %}
      {% assign term_docs = term_docs | push: record %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign sorted = term_docs | sort %}

<!-- {% assign letters = "" | split: "" %}
{% for entry in sorted %}
  {% assign term = entry | split: "||" | first %}
  {% assign letter = term | slice: 0, 1 | upcase %}
  {% unless letters contains letter %}
    {% assign letters = letters | push: letter %}
  {% endunless %}
{% endfor %}

<nav class="term-nav skt">
  {% for letter in letters %}
    <a href="#letter-{{ letter }}">{{ letter }}</a>{% unless forloop.last %} ·{% endunless %}
  {% endfor %}
</nav> -->

## Index of terms

Note: This is a curated list of {{ sorted.size }} terms. It is not 
a replacement for the table of contents.

{% assign shown_letters = "" | split: "" %}

<div class="container my-4">
  <label for="term-search" class="form-label">Search Term:</label>
  <select id="term-search" class="form-select" style="width: 100%;">
    <option value="">-- Select a term --</option>
    {% assign seen_terms = "" | split: "" %}
    {% for entry in sorted %}
      {% assign term = entry | split: "||" | first %}
      {% unless seen_terms contains term %}
        <option value="{{ term }}">{{ term }}</option>
        {% assign seen_terms = seen_terms | push: term %}
      {% endunless %}
    {% endfor %}
  </select>
</div>

<script>
  $(document).ready(function () {

const hash = decodeURIComponent(window.location.hash.substring(1)); // Remove '#' and decode
if (hash) {
  $('.term-content').hide(); // Hide all entries first
  $('#div-term-' + hash).show();
}

function normalizeITRANS(params, data) {
  if (!params.term || !data.text) return data;

  // Transliterate user input (ITRANS) to Devanagari
  const devanagariInput = Sanscript.t(params.term, 'itrans', 'devanagari');

  // Check if option text includes the transliterated input
  if (data.text.includes(devanagariInput)) {
    return data;
  }

  // Return null to filter out this option if no match
  return null;
}

    const $dropdown = $('#term-search');

    $dropdown.select2({
      placeholder: 'Start typing a term (e.g., mokSha for मोक्ष)...',
      allowClear: true,
      matcher: normalizeITRANS
    });

    $dropdown.on('change', function () {
      const selected = $(this).val();
      if (selected) {
        const el = document.getElementById('div-term-' + selected);
        $('.term-content').hide();
        $('#div-term-' + selected).show();
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });

    // ✅ Wait for dropdown to open, then focus the actual input field
    $dropdown.on('select2:open', function () {
      document.querySelector('.select2-container--open .select2-search__field').focus();
    });

    // 🌟 Trigger focus if URL has ?focus=1
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('focus') === '1') {
      setTimeout(() => {
        $dropdown.select2('open');
      }, 100); // Short delay to ensure Select2 is fully initialized
    }
  });
</script>



<div class="skt">
{% assign current_term = "" %}

{% for entry in sorted %}
  {% assign parts = entry | split: "||" %}
  {% assign term = parts[0] %}
  {% assign title = parts[1] %}
  {% assign url = parts[2] %}

  {% assign term_letter = term | slice: 0, 1 | upcase %}
  {% if term != current_term %}
    {% if forloop.first == false %}
      </ul></div>
    {% endif %}
    {% unless shown_letters contains term_letter %}
      <p id="letter-{{ term_letter }}"></p>
      {% assign shown_letters = shown_letters | push: term_letter %}
    {% endunless %}
    <div id="div-term-{{ term }}" class="term-content" style="display: none;">
    <p id="{{ term }}">{{ term }}</p>
    <ul>
    {% assign current_term = term %}
  {% endif %}
    <li><a href="{{ url }}">{{ title }}</a></li>

  {% if forloop.last %}
    </ul></div>
  {% endif %}
{% endfor %}
</div>
