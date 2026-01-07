---
old_layout: default
permalink: /publish/sagara_raw
title: विचारसागरः
---

{% if jekyll.environment == "development" %}

<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="../../assets/sagara_publish_raw.css">
</head>
<body>

<h1 class="title">{{page.title}}</h1>

{% for item in site.sagara %}
  {% include avarta_head_publish.html avarta_num=item.avarta_num %}

  {% if item.skip_title != true %}<h2>{{ item.title | markdownify | strip_html }}</h2>{% endif %}
  {{ item.content }}

  {% include tags-publish.html index_terms=item.index_terms link_terms=item.link_terms %}

{% endfor %}

</body></html>

{% endif %}
