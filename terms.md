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
      {% assign record = term | append: "||" | append: "विचारचन्द्रोदये " | append: doc.kala_number | append: "." | append: doc.question_number | append: " -- " | append: doc.question_text_skt | append: doc.glossary_heading_skt | append: "||" | append: doc.url %}
      {% assign term_docs = term_docs | push: record %}
    {% endfor %}
  {% endif %}
{% endfor %}


{% assign sorted = term_docs | sort %}

## Index / Terms

Note: This is a manually curated list of terms. It is not 
a replacement for the table of contents.

<div class="skt">
{% assign current_term = "" %}
{% for entry in sorted %}
  {% assign parts = entry | split: "||" %}
  {% assign term = parts[0] %}
  {% assign title = parts[1] %}
  {% assign url = parts[2] %}

  {% if term != current_term %}
    {% if forloop.first == false %}
      </ul>
    {% endif %}
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
