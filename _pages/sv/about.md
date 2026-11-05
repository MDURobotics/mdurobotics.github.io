---
ref: about
title: "Om oss"
label: "Vilka vi är"
permalink: /sv/about/
---

<!-- TODO: gruppens historik, forskningsinriktning, kontakt och lediga tjänster -->

## Personer

<ul class="people">
{% for p in site.data.people.members %}
  <li class="person">
    <a class="person__name" href="{{ p.url }}">{{ p.name }}</a>
    <span class="person__role">{% if page.lang == "sv" %}{{ p.role_sv | default: p.role }}{% else %}{{ p.role }}{% endif %}</span>
    {% if p.orcid %}<a class="person__link" href="https://orcid.org/{{ p.orcid }}">ORCID</a>{% endif %}
  </li>
{% endfor %}
</ul>
