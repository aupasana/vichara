---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /gita
page_numbers:
 - 1
 - 26
 - 81
 - 118
 - 155
 - 180
 - 214
 - 237
 - 262
 - 289
 - 316
 - 354
 - 367
 - 397
 - 418
 - 436
 - 453
 - 475 
---

## <img src="/assets/images/icons/gopuram-solid.svg" class="icon-head"> bhagavad gītā

The śrīdharī vyākhyā is a simple samskr̥ta bhāṣya on the gīta. It has been translated 
by [sw. vīreśvarānanda and published by the
ramakrishna math](https://archive.org/details/bhagavad-gita-sridhara-gloss-2nd-edition-swami-vireswarananada/mode/1up?view=theater).

{% assign chapter_names = "अर्जुनविषादयोगः,साङ्ख्ययोगः,कर्मयोगः,ज्ञानयोगः,कर्मसंन्यासयोगः,अध्यात्मयोगः,ज्ञानविज्ञानयोगः,महापुरुषयोगः,राजविद्याराजगुह्ययोगः,विभूतियोगः,विश्वरूपदर्शनयोगः,भक्तियोगः,प्रकृतिपुरुषविवेकयोगः,गुणत्रयविभागयोगः,पुरुषोत्तमयोगः,दैवासुरसम्पद्विभागयोगः,श्रद्धात्रयविभागयोगः,संन्यासयोगः" | split: "," %}

<div class="skt">
<ul>
{% for page_num in page.page_numbers %}
  {% assign chapter_index = forloop.index0 %}
  {% assign chapter_name = chapter_names[chapter_index] %}
  {% assign page_num_with_offset = page_num | plus: 32 %}
  <li>
    <a href="https://archive.org/details/bhagavad-gita-sridhara-gloss-2nd-edition-swami-vireswarananada/page/n{{ page_num_with_offset }}/mode/1up?view=theater">
      अध्यायः {{ chapter_index | plus: 1 }} -- {{ chapter_name }}
    </a>
  </li>
{% endfor %}
</ul>
</div>
