---
layout: page
permalink: /sagara/
---

## <img src="/assets/images/icons/water-solid.svg" class="icon-head"> vicāra sāgara

The saṁskr̥ta vicāra sāgara is the ocean of vedāntic inquiry.
This prakaraṇa grantha was composed by sw. vāsudeva brahmendra in saṁskr̥ta, 
based on pt. niścaladāsa-jī's hindi work of the same name.

- <a href="/chandra/introduction">preamble / introduction to the saṁskr̥ta vicāra sāgara</a>
- [śrīmukham to the publication](/essays/sagara/shrimukham)
- [flat index of āvartas](/sagara/avarta)
- [curated index of terms](/terms)

{% if jekyll.environment == "development" %}
Debugging:

- [Publication view (all āvartas)](/publish/sagara_web)
- [Translation pending](/sagara/pending)
{% endif %}

<div class="skt">

<div markdown=1>
तरङ्गाः --॥ 
[१](#1-39)॥ 
[२](#40-108)॥ 
[३](#109-121)॥ 
[४](#122-225)॥ 
[५](#226-316)॥ 
[६](#317-463)॥ 
[७](#464-538)॥ 
</div>

{% assign indent_level = 0 %}

{% for p in site.sagara %}

{% assign p_index = p.avarta_num | plus: 0 %}
{% assign matching_sections_start = site.data.sagara_sections | where: "start", p_index | sort: "start" %}
{% assign matching_sections_end = site.data.sagara_sections | where: "end", p_index | sort: "start" | reverse %}

{% for section in matching_sections_start %}

{% if indent_level == 0 %}
<br/><h1 id="{{section.start}}-{{section.end}}"> {{ section.label }}</h1><br/>
{% else %}
{% assign range = section.start | append: "-" | append: section.end %}
[ {% include to_devanagari_numbers.html text=range %} {{ section.label }}
    {% if jekyll.environment == "development" %}
<span class="tree-toggle" data-bs-toggle="collapse" data-bs-target="#node-{{section.start}}-{{section.end}}" role="button" aria-expanded="false" aria-expanded="true" aria-controls="node-{{section.start}}-{{section.end}}"></span>
    {% endif %}
{% endif %}

{% if indent_level > 0 %}
<div id="{{section.start}}-{{section.end}}" class="nested-inline indent-{{indent_level}}">
<div class="collapse show" id="node-{{section.start}}-{{section.end}}">
<div class="ps-3">

{% endif %}
{% assign indent_level = indent_level | plus: 1 %}
{% endfor %}
<a href="{{p.url}}">{{p.title}}</a><br/>

{% for section in matching_sections_end %}
{% if indent_level > 1 %}
</div></div>
</div>
{% endif %}

{% if indent_level >= 1 %} 
    {% assign indent_level = indent_level | plus: -1 %}
{% endif %}
{% if indent_level >= 1 %} 
  {% assign range = section.start | append: "-" | append: section.end %}
] {% include to_devanagari_numbers.html text=range %} {{ section.label }}<br/>
{% endif %}
{% endfor %}

{% if matching_sections_end.size > 1 %}
<br />
{% endif %}

{% endfor %}

