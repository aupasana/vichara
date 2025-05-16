---
layout: page
permalink: /chandra/publish
title: विचारचन्द्रोदयः
---

{% if jekyll.environment == "development" %}

<div class="skt"><h1>{{page.title}}</h1></div>


{% for item in site.kala_question %}

<div class="skt" markdown="1">
<h2>{{item.kala_number}}.{{item.question_number}} {{ item.question_text_skt }} {{ item.glossary_heading_skt}}</h2>
</div>

<div class="translation" markdown="1">
Topic: {{item.question_text}}
</div>

{% if item.no_split == true %}
  {{ item.content }}
{% else %}
  {% assign sections = item.content | split: '<!-- split -->' %}
  <div class="skt" markdown="1">{{ sections[0] | markdownify }}</div><p/>
  <div class="translation" markdown="1">
    {{ sections[1] | markdownify }}
  </div>

{% endif %}

{% endfor %}
{% endif %}