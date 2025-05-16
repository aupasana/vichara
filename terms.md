---
layout: page
permalink: /terms
---

{% assign term_docs = "" | split: "" %}

{% for doc in site.avarta %}
  {% if doc.index_terms %}
    {% for term in doc.index_terms %}
      {% assign record = term | append: "||" | append: "विचारसागरे " | append: doc.title | append: "||" | append: doc.url %}
      {% assign term_docs = term_docs | push: record %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% for doc in site.kala_question %}
  {% if doc.index_terms %}
    {% for term in doc.index_terms %}
      {% assign normal_record = term | append: "||" | append: "विचारचन्द्रोदये " | append: doc.kala_number | append: "." | append: doc.question_number | append: " -- " | append: doc.question_text_skt | default: glossary_name | append: "||" | append: doc.url %}

      {% assign glossary_record = term | append: "||" | append: "विचारचन्द्रोदयकोषः" | append: " -- " | append: doc.glossary_heading_skt | default: glossary_name | append: "||" | append: doc.url %}

      {% if doc.glossary_heading_skt %}
        {% assign record = glossary_record %}
      {% else %}
        {% assign record = normal_record %}
      {% endif %}

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

{% assign sorted = term_docs | sort %}

{% assign letters = "" | split: "" %}
{% for entry in sorted %}
  {% assign term = entry | split: "||" | first %}
  {% assign letter = term | slice: 0, 1 | upcase %}
  {% unless letters contains letter %}
    {% assign letters = letters | push: letter %}
  {% endunless %}
{% endfor %}

<nav class="term-nav">
  {% for letter in letters %}
    <a href="#letter-{{ letter }}">{{ letter }}</a>{% unless forloop.last %} · {% endunless %}
  {% endfor %}
</nav>

## Index of terms

Note: This is a manually curated list of {{ sorted.size }} terms. It is not 
a replacement for the table of contents.

{% assign shown_letters = "" | split: "" %}

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
      </ul>
    {% endif %}
    {% unless shown_letters contains term_letter %}
      <p id="letter-{{ term_letter }}"></p>
      {% assign shown_letters = shown_letters | push: term_letter %}
    {% endunless %}
    <p id="{{ term }}">{{ term }}</p>
    <ul>
    {% assign current_term = term %}
  {% endif %}
    <li><a href="{{ url }}">{{ title }}</a></li>

  {% if forloop.last %}
    </ul>
  {% endif %}
{% endfor %}
</div>
