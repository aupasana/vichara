---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /upanishads/mantras
---

## <img src="/assets/images/icons/om-solid.svg" class="icon-head"> upaniṣad mantras

<div class="skt">
{% for p in site.upanishads %}
<a href="{{p.url}}">{{p.title}}</a><br/>
{% endfor%}
</div>