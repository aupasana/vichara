---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
skip_mangala: true
---

<div class="kesari">
    <img src="/assets/images/simha_garjana.svg" alt="vedanta kesari" height="150" class="kesari-image" />
    <div>
    <div class="skt">
    तावद्गर्जन्ति शास्त्राणि जम्बुका विपिने यथा।<br/>
    न गर्जन्ति महाशक्तिर्यावद्वेदान्तकेसरी॥
    </div>
    "In the forest of thought, the jackals of numerous philosophical views continue
to howl, until the lion of vedānta sets forth it's triumphant roar."
    </div>
</div>

<div class="mangala" markdown="1">
॥ॐ गुरुपरमात्मने नमः॥
</div><p/>

## The vicāra candrodaya

<div>
The vicāra candrodaya is the moon that rises out of the ocean of vedāntic inquiry.
This prakaraṇa grantha was composed by pt. pītāmbar-jī in hindi. 
We have translated it into saṁskr̥t, along with an english gloss.
</div>

### Introduction

- [preamble / introduction to the saṁskr̥ta vicāra candrodaya]({% link chandra/introduction.md %})
- [tattva bodha - a primer of vedānta terminology]({% link tattva_bodha.md %})

The vicāra candrodaya spans 427 topics (248 questions + 179 footnotes) across the 15 chapters (kalās). 
This is followed by a glossary of terms in the last kalā.

### The 16 kalās

<ul>
 <li><a href="{% link chandra/big_picture.md %}">the big picture & sādhanas</a></li>
{% for kala_item in site.kala %}
    {% if kala_item.sections and kala_item.skip_publish != true %}
<li><a href="{{ kala_item.url }}">kalā {{kala_item.kala_number}} - {{kala_item.description}} (<span class="skt_span">{{kala_item.description_skt}}</span>)</a></li>
    {% else %}
<li>kalā {{kala_item.kala_number}} - {{kala_item.description}} (<span class="skt_span">{{kala_item.description_skt}}</span>)</li>
    {% endif %}
    {% endfor %}
</ul>

- [all diagrams]({% link chandra/diagrams.md %})

## Other essays

- [classification of jñāna -- bhāsyatva / āśrayatva / adhīnatva etc]({% link essays/pratyaksha-bhasya.md %})
- [contents of the vicāra sāgara]({% link sagara/index.md %})