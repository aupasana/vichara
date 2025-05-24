---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
skip_mangala: true
permalink: /chandra/
---

## <img src="/assets/images/icons/moon-solid.svg" class="icon-head"> vicāra candrodaya

The vicāra candrodaya is the moon that rises out of the ocean of vedāntic inquiry.
This prakaraṇa grantha was composed by pt. pītāmbar-jī in hindi. 
The saṁskr̥t and english translations shared here are original derivative works.

This grantha spans 427 topics (248 questions + 179 footnotes) across the first 15 chapters (kalās).
The sixteenth kalā is a glossary of terms, grouped into collections.

<div class="note-box">
<img src="/assets/images/icons/spinner-solid.svg" width="20" height="20"/>
This is a work in progress. 
</div>

<ul>
 <li><a href="{% link chandra/introduction.md %}">preamble / introduction to the saṁskr̥ta vicāra candrodaya</a></li>
 <li><a href="essays/big_picture">the big picture & sādhanas</a></li>
</ul>

{% if jekyll.environment == "development" %}
Debugging:

- [Publication view (all topics)](/chandra/publish)
{% endif %}


<ul>
{% for kala_item in site.kala %}
    {% if kala_item.skip_publish != true %}
<li><a href="{{ kala_item.url }}">kalā {{kala_item.kala_number}} - {{kala_item.description}} (<span class="skt_span">{{kala_item.description_skt}}</span>)</a></li>
    {% else %}
<li>kalā {{kala_item.kala_number}} - {{kala_item.description}} (<span class="skt_span">{{kala_item.description_skt}}</span>)</li>
    {% endif %}
    {% endfor %}
</ul>

- [all diagrams]({% link chandra/diagrams.md %})

