---
layout: default
permalink: /sagara/publish
title: विचारसागरः
---

{% if jekyll.environment == "development" %}
<div class="skt" markdown="1">

<h1>{{page.title}}</h1>

<ul>
{% for item in site.sagara %}
  <li><a href="#{{ item.id }}">{{ item.title | markdownify | strip_html }}</a></li>
{% endfor %}
</ul>

{% for item in site.sagara %}
  <div id="{{ item.id }}"></div>
  {% if item.skip_title != true %}<h2>{{ item.title | markdownify }}</h2>{% endif %}
  {{ item.content }}
{% endfor %}

</div>
{% endif %}