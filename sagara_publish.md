---
layout: page
permalink: /sagara/publish
title: विचारसागरः
---

{% if jekyll.environment == "development" %}
<div class="skt" markdown="1">

<h1>{{page.title}}</h1>

<ul>
{% for item in site.avarta %}
  <li><a href="#{{ item.id }}">{{ item.title }}</a></li>
{% endfor %}
</ul>

{% for item in site.avarta %}
  <div id="{{ item.id }}">
  {% if item.skip_title != true %}<h2>{{ item.title }}</h2>{% endif %}
  {{ item.content }}
{% endfor %}

</div>
{% endif %}