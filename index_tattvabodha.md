---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /tattvabodha
---

## <img src="/assets/images/icons/start-solid.svg" class="icon-head"> tattva bodha

The tattva bodha is a "first text of vedānta" which describes
essential vedānta terminology. It is worth revising
before studying the vicāra candrodaya. 

Part 0

- [An introduction to śāstra (based on the prasthāna bheda)](/essays/prasthana-bheda)

{% assign current_section = "" %}

{% for question_item in site.tb_question %}
  {% if question_item.section_number != current_section %}
    {% unless forloop.first %}
      </ul>
    {% endunless %}

    {% assign matched_section = site.tb_section | where: "section_number", question_item.section_number | first %}

part {{question_item.section_number}} - {{matched_section.section_title}} (<span class="skt_span">{{matched_section.section_title_skt}}</span>)
<ul>

    {% assign current_section = question_item.section_number %}
  {% endif %}

  <li>
    <a href="{{question_item.url}}">{{question_item.section_number}}.{{question_item.question_number}}</a>: {{question_item.question_text}}
    <span class="skt_span">{{question_item.question_text_skt}}</span>
  </li>
{% endfor %}

</ul>

