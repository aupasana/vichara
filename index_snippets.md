---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /snippets
---

## snippets

Here are some memorable quotes
from the granthas on this site -- 
hopefully suitable for mananam.
They will keep getting added 
incrementally.

{% assign sorted_snippets = site.snippets | sort: "url" %}

<div class="skt">
<ul>
{% for item in sorted_snippets %}
<li><a href="{{item.url}}">{{ item.title | markdownify | remove: '<p>' | remove: '</p>' }}</a>{% if item.source %} <span class="snippet-index-source">-- {{item.source}}</span>{% endif %}</li>
{% endfor %}
</ul>
</div>
