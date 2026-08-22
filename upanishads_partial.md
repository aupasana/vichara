---
layout: default
permalink: /upanishad/excerpts
title: उपनिषन्मन्त्राः प्रसिद्धाः केचन
---

<div class="skt">

<h1>{{page.title}}</h1>

{% for item in site.upanishads %}
  {% if item.permalink contains '/partial' %}
<p/><a href="{{ item.url }}">{{ item.title | markdownify | strip_html }}</a>
    {% if item.index_terms and item.index_terms.size > 1 %}<br/>
    {% for term in item.index_terms %}
    {{term}}। 
    {% endfor %}<br/>
    {% endif %}
  {% endif %}
{% endfor %}

</div>
