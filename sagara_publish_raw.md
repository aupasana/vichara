---
old_layout: default
permalink: /sagara/publish/raw
title: विचारसागरः
---

<html>
<body>

{% if jekyll.environment == "development" %}

<h1>{{page.title}}</h1>

{% for item in site.sagara %}
  {% if item.skip_title != true %}<h2>{{ item.title | markdownify | strip_html }}</h2>{% endif %}
  {{ item.content }}
{% endfor %}

{% endif %}

</body></html>