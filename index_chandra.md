---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
skip_mangala: true
permalink: /chandra
in_progress: true
---

## <img src="/assets/images/icons/moon-solid.svg" class="icon-head"> vicāra candrodaya

The vicāra candrodaya is the moon that rises out of the ocean of vedāntic inquiry.
This prakaraṇa grantha was composed by pt. pītāmbar-jī in hindi. 
The saṁskr̥t and english translations shared here are original derivative works.

This grantha spans 427 topics (248 questions + 179 footnotes) across the first 15 chapters (kalās).
The sixteenth kalā is a glossary of terms, grouped into collections.

<ul>
 <li><a href="{% link chandra/introduction.md %}">preamble / introduction to the saṁskr̥ta vicāra candrodaya</a></li>
 <li><a href="essays/big_picture">the big picture & sādhanas</a></li>
</ul>

{% if jekyll.environment == "development" %}
Debugging:

- [Publication view (all topics)](/chandra/publish)
{% endif %}

{% assign current_kala = "" %}
{% assign current_section = "" %}

{% for question_item in site.chandra_question %}
  {% assign this_kala = question_item.kala_number %}
  {% assign this_section = question_item.section_number %}

  {% if this_kala != current_kala or this_section != current_section %}
    {% unless forloop.first %}
      </ul>
    {% endunless %}

    {% assign matched_section = site.chandra_section | where: "kala_number", this_kala | where: "section_number", this_section | first %}

    {% assign matched_kala = site.chandra | where: "kala_number", this_kala | first %}

    {% if this_kala != current_kala %}
<h3><a href="{{matched_kala.url}}">{{ matched_kala.description }} ( <span class="skt_span">{{ matched_kala.description_skt }}</span> )</a></h3>
    {% endif %}

    {% if matched_section %}
<a href="{{matched_section.url}}">{{this_kala}}.{{this_section}} - <span class="skt_span">{{matched_section.section_title_skt}}</span> ({{matched_section.section_title}})</a>
    {% else %}
part {{this_kala}}.{{this_section}} - (no matching section)
    {% endif %}
<ul>

    {% assign current_kala = this_kala %}
    {% assign current_section = this_section %}
  {% endif %}

  <li>
    <a href="{{question_item.url}}">{{question_item.kala_number}}.{{question_item.question_number}}</a>: {{question_item.question_text}}
    <span class="skt_span">{{question_item.question_text_skt}}</span>
  </li>
{% endfor %}

</ul>