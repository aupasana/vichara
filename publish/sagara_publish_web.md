---
layout: default
permalink: /publish/sagara_web
title: विचारसागरः
---

{% if jekyll.environment == "development" %}

<div class="skt">
<h1>{{page.title}}</h1>

{% for item in site.sagara %}
  {% include avarta_head_publish.html avarta_num=item.avarta_num %}

  {% if item.skip_title != true %}<h2>{{ item.title | markdownify | strip_html }}</h2>{% endif %}
  {{ item.content }}
  <hr/>
{% endfor %}
</div>

{% endif %}

