---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /publish/tattvabodha_web
title: तत्त्वबोधः
---

<div class="skt" markdown="1">
<h1>{{page.title}}</h1>
</div>

{% for question_item in site.tb_question %}

  <div class="item_question" id="{{question_item.section_number}}.{{ question_item.question_number }}" >{{question_item.section_number}}.{{ question_item.question_number }}: <span class="item_question_eng">{{ question_item.question_text }}<br/></span>
  <span class="skt_span">{{ question_item.question_text_skt }}</span></div><p/>
    {% if question_item.no_split == true %}
      {{ question_item.content }}
    {% else %}
      {% assign sections = question_item.content | split: '<!-- split -->' %}
<div class="skt" markdown="1">{{ sections[0] | markdownify }}</div><p/>
<div class="translation" markdown="1">
  {{ sections[1] | markdownify }}
</div>
    {% endif %}

{% endfor %}
