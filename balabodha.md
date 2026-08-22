---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /balabodha
in_progress: true
---

## <img src="/assets/images/icons/start.svg" class="icon-head"> bāla bodha

The bāla bodha is an introductory text of vedānta by pītāmbar jī in hindi. 
Thi is a very early partial preview.

{% assign current_upadesha = "" %}

{% for question_item in site.balabodha_question %}
  {% if question_item.upadesha_number != current_upadesha %}
    {% unless forloop.first %}
      </ul>
    {% endunless %}

    {% assign matched_upadesha = site.balabodha_upadesha | where: "upadesha_number", question_item.upadesha_number | first %}

part {{question_item.upadesha_number}} - {{matched_upadesha.upadesha_title}} (<span class="skt_span">{{matched_upadesha.upadesha_title_skt}}</span>)
<ul>

    {% assign current_upadesha = question_item.upadesha_number %}
  {% endif %}

  <li>
    <a href="{{question_item.url}}">{{question_item.upadesha_number}}.{{question_item.question_number}}</a>: {{question_item.question_text}}
    <span class="skt_span">{{question_item.question_text_skt}}</span>
  </li>
{% endfor %}

</ul>

