---
old_layout: default
permalink: /publish/upanishads_raw
title: उपनिषन्मणिप्रभा
---

{% if jekyll.environment == "development" %}

<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="../../assets/sagara_publish_raw.css">
</head>
<body>

<h1 class="title">{{page.title}}</h1>

{% for item in site.upanishads %}
  {% if item.mulam != true %}
    {% if item.skip_title != true %}<h2>{{ item.title | markdownify | strip_html }} – </h2>{% endif %}
    {{ item.content }}
    <hr/>
  {% endif %}
{% endfor %}

</body></html>

{% endif %}

