---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /tattvabodha
---

## <img src="/assets/images/icons/start.svg" class="icon-head"> tattva bodha

The tattva bodha is a "first text of vedānta" which describes
essential vedānta terminology. It is worth revising
before studying the vicāra candrodaya. 

Part 0

- [An introduction to śāstra (based on the prasthāna bheda)](/essays/prasthana-bheda)


{% for tb_item in site.tb_section %}
    {% if tb_item.questions and tb_item.skip_publish != true %}
<a href="{{ tb_item.url }}" id="sec{{tb_item.section_number}}">part {{tb_item.section_number}} - {{tb_item.section_title}} (<span class="skt_span">{{tb_item.section_title_skt}}</span>)</a>

<ul>
  {% for question_id in tb_item.questions %}
    {% assign question_item = site.tb_question | where: "tb_question_id", question_id | first %}

    {% if question_item %}
      <li><a href="/tattvabodha/{{tb_item.section_number}}#{{question_item.section_number}}.{{question_item.question_number}}">{{question_item.section_number}}.{{question_item.question_number}}</a>: {{question_item.question_text}}
      <span class="skt_span">{{question_item.question_text_skt}}</span></li>
    {% else %}
      <li>Missing question: {{ question_id }}</li>
    {% endif %}
    
  {% endfor %}
</ul>

    {% else %}
<ul><li>part {{tb_item.section_number}} - {{tb_item.section_title}} (<span class="skt_span">{{tb_item.section_title_skt}}</span>)</li></ul>
    {% endif %}
{% endfor %}

