---
layout: default
permalink: /sagara/draft
title: विचारसागरे अनुवादनीयाः आवर्ताः
---

{% if jekyll.environment == "development" %}
<div class="skt" markdown="1">

<h1>{{page.title}}</h1>

<ul>
{% for item in site.sagara %}
  {% if item.draft == true %}
<li><a href="{{ item.url }}">{{ item.title | markdownify | strip_html }}</a></li>
  {% endif %}
{% endfor %}
</ul>

</div>
{% endif %}