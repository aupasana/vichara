---
layout: default
permalink: /publish/upanishads_web
title: उपनिषदः
---

{% if jekyll.environment == "development" %}

<div class="skt">
<h1>{{page.title}}</h1>

{% for item in site.upanishads %}
  {% if item.mulam != true %}
    {% if item.skip_title != true %}<p>{{ item.title | markdownify | strip_html }} – </p>{% endif %}
    {{ item.content }}
    <hr/>
  {% endif %}
{% endfor %}
</div>

{% endif %}

