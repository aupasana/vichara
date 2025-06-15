---
layout: default
permalink: /sagara/pending
title: विचारसागरे अनुवादनीयाः आवर्ताः
---

{% if jekyll.environment == "development" %}
<div class="skt" markdown="1">

<h1>{{page.title}}</h1>

<ul>
{% for item in site.sagara %}
  {% unless item.content contains "translation-inline" %}
<li><a href="{{ item.url }}">{{ item.title | markdownify | strip_html }}</a></li>
  {% endunless %}
{% endfor %}
</ul>

</div>
{% endif %}