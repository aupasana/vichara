---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

<div>
The tattva bodha is the most basic prakaraṇa grantha, which
provides short definitions of the most common vedāntic 
terminology. It is a good `first text of vedānta`.

<ul>
{% for tb_item in site.tb_section %}
    {% if tb_item.questions and tb_item.skip_publish != true %}
<li><a href="{{ tb_item.url }}" id="sec{{tb_item.section_number}}">part {{tb_item.section_number}} - {{tb_item.section_title}} (<span class="skt_span">{{tb_item.section_title_skt}}</span>)</a></li>

        <ul>
        {% for question_id in tb_item.questions %}
          {% assign question_item = site.tb_question | where: "tb_question_id", question_id | first %}

          {% if question_item %}
            <li><a href="/tattva_bodha/{{tb_item.section_number}}#{{question_item.section_number}}.{{question_item.question_number}}">{{question_item.section_number}}.{{question_item.question_number}}</a>: {{question_item.question_text}}
            <span class="skt_span">{{question_item.question_text_skt}}</span></li>
          {% else %}
            <li>Missing question: {{ question_id }}</li>          
          {% endif %}
          
        {% endfor %}
        </ul>

    {% else %}
<li>part {{tb_item.section_number}} - {{tb_item.section_title}} (<span class="skt_span">{{tb_item.section_title_skt}}</span>)</li>
    {% endif %}
{% endfor %}
</ul>

