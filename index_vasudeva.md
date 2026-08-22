---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /vasudeva
in_progress: true
---

## <img src="/assets/images/icons/lightbulb-solid.svg" class="icon-head"> laghu vasudeva mananam

The laghu vāsudeva mananam is a short prakaraṇa grantha which summarizes the vedanta prameya. It was composed by Sw. vāsudevānanda. 
An extract from the śrīmukha by Jagadguru śrīmad abhinava vidyātīrtha svāmī to the published Tamil translation is given below.

{% assign sorted_vasudeva = site.vasudeva | sort: "varnaka_num" %}

<div class="skt">
<ul>
{% for item in sorted_vasudeva %}
<li><a href="{{item.url}}">{{item.title}}</a></li>
{% endfor %}
</ul>
</div>