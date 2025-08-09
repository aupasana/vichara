---
layout: default
permalink: /sagara/avarta
title: विचारसागरे आवर्ताः
---
<div class="skt">

<h1>{{page.title}}</h1>

<ul>
{% for item in site.sagara %}
<li><a href="{{ item.url }}">{{ item.title | markdownify | strip_html }}</a></li>
{% endfor %}
</ul>

</div>
