---
layout: markdown
title: EVMavericks
permalink: /evmavericks/
---




<section markdown=1>

{% for group in site.data.evmavericks %}
{{group.title}}
  {% for item in group.items %}
- [{{item.text}}]({{item.link}}) <span class="small">{{item.extra}}</span>
  {%- endfor %}
{% endfor %}

</section>
