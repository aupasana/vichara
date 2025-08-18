---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /upanishads
---

## <img src="/assets/images/icons/om-solid.svg" class="icon-head"> upaniṣads

The prasāda and maniprabhā are simple commentaries on the upaniṣads that unfold
their meaning following the saṅkara bhāṣya. Here are their reference editions.

- upaniṣad prasāda by sw. bhāskarānanda ([part 1](https://archive.org/details/UpanishatPrasada), [part 2](https://archive.org/details/VARp_dash-upanishad-with-subodh-tika-by-swami-bhaskaranand-sarasvati-1933-master-kheladilal-and-sons))
- upaniṣad maniprabhā by sw. amaradāsa ([link](https://archive.org/details/ekadasopanishadah-with-maniprabha-tika-of-swami-amaradasa-udasina-1910-nsp))

<div class="container mt-5">
  <div class="row g-4 align-items-stretch">

{% include index_card.html number=1 icon="om" title="īśāvāsya" description="with prasāda & maṇiprabhā" link="/isha" %}

{% include index_card.html number=2 icon="om" title="kena" description="with maṇiprabhā" link="/kena" %}

{% include index_card.html number=3 icon="om" title="excerpts" description="selected mantras which are quoted often" link="/upanishad/excerpts" %}

  </div>
</div>
<br/>

<div class="skt">
<h2>मन्त्राः</h2>
{% for p in site.upanishads %}
<a href="{{p.url}}">{{p.title}}</a><br/>
{% endfor%}
</div>