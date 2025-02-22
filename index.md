---
layout: markdown
title: Overview
---


{%- assign announcements_size = site.data.announcements | size -%}
{%- if announcements_size > 0 -%}
  <div class="mb-3">
    <h6>Announcements</h6>
    <section class="tight" style="width: fit-content;">
      <ul>
        {%- for announcement in site.data.announcements -%}
          <li>{{announcement.message | markdownify | remove: '<p>' | remove: '</p>'}}</li>
        {%- endfor -%}
      </ul>
    </section>
  </div>
{%- endif -%}


<div class="row g-4">
  <div class="col mb-3">
    <h6>Leaderboard</h6>
    {% include partials/leaderboard.html limit=10 %}
  </div>

  <div class="col mb-3">
    <h6>Upcoming Events</h6>
    {% include partials/events.html limit=10 %}
  </div>

  <div class="col mb-3">
    <h6 class="pb-1">Daily Threads</h6>
    <section class="mt-4" style="width:fit-content; min-width:315px;">
    {%- assign dailies = site.data.dailies | sort: 'date' | reverse -%}
    <ul>
      {%- for daily in dailies limit:10 -%}
        {%- assign date = daily.date | date: "%B %d, %Y" -%}
        {%- assign title = daily.title -%}
        {%- assign link = daily.link -%}
        {%- assign comments = daily.comments -%}
        <li><a href="{{link}}">{{date}} &nbsp;({{comments}} comments)</a></li>
      {%- endfor -%}
    </ul>
  </section>
  </div>
</div>

