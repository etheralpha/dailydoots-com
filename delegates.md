---
layout: markdown
title: Delegates
permalink: /delegates/
---


Delegate your votes to a member of the EthFinance community. 

<small class="opacity-75">
  Are you a delegate and not listed? 
  Send a DM to [u/hanniabu](https://reddit.com/u/hanniabu) to get added.
</small>

<div class="table-responsive" markdown=1>

Username | Project | Info
---------|---------|------

{%- for delegate in site.data.delegates %}
  {% assign username = delegate.username -%}
  {%- assign project = delegate.project -%}
  {%- assign link = delegate.profile -%}
{{username}} | {{project}} | [View details and delegate]({{link}}) {% endfor %}

</div>

