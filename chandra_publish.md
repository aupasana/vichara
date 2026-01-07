---
layout: page
permalink: /chandra/publish
title: विचारचन्द्रोदयः
---

{% if jekyll.environment == "development" %}

<div class="skt"><h1>{{page.title}}</h1></div>

{% for item in site.chandra_question %}

<div class="skt" markdown="1">
<h2><span class="">{{item.kala_number}}.{{item.question_number}}</span> {{ item.question_text_skt }} {{ item.question_text_skt}}</h2>
</div>

{% assign source = item.content %}
{% assign after_start = source | split: '<!-- skt-start -->' %}
{% assign after_start = after_start[1] %}
{% assign before_end = after_start | split: '<!-- skt-end -->' %}
{% assign skt_content = before_end[0] %}

<div class="skt" markdown="1">
  {{ skt_content | markdownify }}
</div><p/><hr/>

{% endfor %}
{% endif %}