---
layout: markdown
title: Profiles
permalink: /profiles/
---


A list of users and their projects to spread awareness of what everyone in the community is working on. 

<small class="opacity-75">
  Working on something cool and not listed? 
  Submit a PR or send a DM to [u/hanniabu](https://reddit.com/u/hanniabu) to get it added.
</small>

<div class="table-responsive" markdown=1>

Username | Description
---------|-------------

{%- for profile in site.data.profiles %}
  {% assign username = profile.username -%}
  {%- assign background = profile.background | replace: '; ', ';<br>' -%}
{{username}} | {{background}} {% endfor %}

</div>

