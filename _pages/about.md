---
ref: about
title: "About us"
label: "Who we are"
permalink: /about/
---

<!-- TODO: lab history, research focus, how to contact us / open positions -->

## People

<ul class="people">
{% for p in site.data.people.members %}
  <li class="person">
    <a class="person__name" href="{{ p.url }}">{{ p.name }}</a>
    <span class="person__role">{% if page.lang == "sv" %}{{ p.role_sv | default: p.role }}{% else %}{{ p.role }}{% endif %}</span>
    {% if p.orcid %}<a class="person__link" href="https://orcid.org/{{ p.orcid }}">ORCID</a>{% endif %}
  </li>
{% endfor %}
</ul>
