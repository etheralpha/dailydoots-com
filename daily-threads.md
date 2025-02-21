---
layout: markdown
title: Historical Daily Threads
permalink: /daily-threads/
---


{%- comment -%}
<!-- 
- date: 2025-01-27
  title: Daily General Discussion - January 27, 2025
  link: https://reddit.com/r/ethereum/comments/1ib27hz/
  comments: 342
 -->
{%- endcomment -%}


{%- assign years = "2025,2024,2023,2022,2021,2020,2019" -%}
{%- assign years = "2025" -%}
{%- assign years = years | split: ',' -%}

{%- assign months = "January,February,March,April,May,June,July,August,September,October,November,December" -%}
{%- assign months = months | split: ',' -%}


{%- assign dailies = site.data.dailies | sort: 'date' -%}
{%- assign limit_count = 5000 -%}
{%- if include.limit -%}
  {%- assign limit_count = include.limit -%}
{%- endif -%}


{%- for year in years -%}
  {%- assign open = '' -%}
  {%- if forloop.first -%}
    {%- assign open = 'open' -%}
  {%- endif -%}
  <details {{open}}>
    <summary>&nbsp;{{year}}</summary>
    {%- for month in months -%}
      {%- assign hidden = true -%}
      <details id="{{month}}{{year}}">
        <summary>&nbsp;{{month}} {{year}}</summary>
        <ul>
          {%- for daily in dailies limit:limit_count -%}
            {%- if daily.title contains year and daily.title contains month -%}
              {%- assign hidden = false -%}
              {%- assign date = daily.date | date: "%B %d, %Y" -%}
              {%- assign title = daily.title -%}
              {%- assign link = daily.link -%}
              {%- assign comments = daily.comments -%}
              <li><a href="{{link}}">{{date}} &nbsp;({{comments}} comments)</a></li>
            {%- endif -%}
          {%- endfor -%}
        </ul>
      </details>
      {%- if hidden == true -%}
        <style>#{{month}}{{year}} {display: none;}</style>
      {%- endif -%}
    {%- endfor -%}
  </details>
{%- endfor -%}



<!-- 2024 -->
<details>
  <summary>&nbsp;2024</summary>
  <details>
    <summary>&nbsp;January 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/18vqcgb/">January 01, 2024 &nbsp;(206 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18wi7t1/">January 02, 2024 &nbsp;(276 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18xc4ml/">January 03, 2024 &nbsp;(293 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18y5x53/">January 04, 2024 &nbsp;(324 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18yznna/">January 05, 2024 &nbsp;(256 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18zt205/">January 06, 2024 &nbsp;(275 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/190lbbx/">January 07, 2024 &nbsp;(273 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/191e4wm/">January 08, 2024 &nbsp;(578 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1927osy/">January 09, 2024 &nbsp;(623 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/193195q/">January 10, 2024 &nbsp;(1083 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/193ukvu/">January 11, 2024 &nbsp;(638 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/194nvno/">January 12, 2024 &nbsp;(534 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/195h4aa/">January 13, 2024 &nbsp;(236 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1968xe8/">January 14, 2024 &nbsp;(255 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1971kkf/">January 15, 2024 &nbsp;(294 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/197vodp/">January 16, 2024 &nbsp;(285 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/198pjar/">January 17, 2024 &nbsp;(427 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/199j5zi/">January 18, 2024 &nbsp;(327 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/19ac5xh/">January 19, 2024 &nbsp;(327 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/19b4wii/">January 20, 2024 &nbsp;(155 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/19bwkm1/">January 21, 2024 &nbsp;(375 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/19cou8k/">January 22, 2024 &nbsp;(714 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/19dhkux/">January 23, 2024 &nbsp;(458 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/19ea76a/">January 24, 2024 &nbsp;(353 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/19f2ia2/">January 25, 2024 &nbsp;(364 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1abbg8a/">January 26, 2024 &nbsp;(294 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ac3zs6/">January 27, 2024 &nbsp;(171 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1acvrm9/">January 28, 2024 &nbsp;(206 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ado855/">January 29, 2024 &nbsp;(218 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1aehg40/">January 30, 2024 &nbsp;(279 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1afauzq/">January 31, 2024 &nbsp;(327 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;February 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ag42lq/">February 01, 2024 &nbsp;(186 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1agwsik/">February 02, 2024 &nbsp;(314 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ahp76i/">February 03, 2024 &nbsp;(191 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1aigxis/">February 04, 2024 &nbsp;(214 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1aj9j2n/">February 05, 2024 &nbsp;(344 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ak2vf5/">February 06, 2024 &nbsp;(477 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1akw42k/">February 07, 2024 &nbsp;(346 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1alov71/">February 08, 2024 &nbsp;(403 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1amhanj/">February 09, 2024 &nbsp;(401 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1an9h36/">February 10, 2024 &nbsp;(291 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ao10pn/">February 11, 2024 &nbsp;(176 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1aot3bs/">February 12, 2024 &nbsp;(422 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1apmglo/">February 13, 2024 &nbsp;(322 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1aqfvsu/">February 14, 2024 &nbsp;(932 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ar8nxe/">February 15, 2024 &nbsp;(490 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1as1h64/">February 16, 2024 &nbsp;(361 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1asuvrp/">February 17, 2024 &nbsp;(208 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1atn3er/">February 18, 2024 &nbsp;(340 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1aug4kx/">February 19, 2024 &nbsp;(572 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1avafsm/">February 20, 2024 &nbsp;(815 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1aw4pug/">February 21, 2024 &nbsp;(405 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1awz3t2/">February 22, 2024 &nbsp;(386 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1axt9ig/">February 23, 2024 &nbsp;(278 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ayn9gi/">February 24, 2024 &nbsp;(234 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1azgo7x/">February 25, 2024 &nbsp;(393 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b0acur/">February 26, 2024 &nbsp;(618 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b14ls9/">February 27, 2024 &nbsp;(527 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b1ys3b/">February 28, 2024 &nbsp;(1088 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b2t640/">February 29, 2024 &nbsp;(569 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;March 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b3n2y3/">March 01, 2024 &nbsp;(384 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b4h3wq/">March 02, 2024 &nbsp;(324 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b59xrs/">March 03, 2024 &nbsp;(316 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b63kgo/">March 04, 2024 &nbsp;(816 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b6y3ja/">March 05, 2024 &nbsp;(856 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b7se02/">March 06, 2024 &nbsp;(666 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b8n4nd/">March 07, 2024 &nbsp;(519 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1b9gurw/">March 08, 2024 &nbsp;(654 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1baap7z/">March 09, 2024 &nbsp;(331 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bb34em/">March 10, 2024 &nbsp;(233 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bbw95o/">March 11, 2024 &nbsp;(780 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bcq1is/">March 12, 2024 &nbsp;(544 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bdk7x0/">March 13, 2024 &nbsp;(776 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1beea63/">March 14, 2024 &nbsp;(557 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bf7318/">March 15, 2024 &nbsp;(452 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bfzcrp/">March 16, 2024 &nbsp;(469 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bgqm1m/">March 17, 2024 &nbsp;(360 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bhjqu7/">March 18, 2024 &nbsp;(707 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bidash/">March 19, 2024 &nbsp;(563 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bj6k75/">March 20, 2024 &nbsp;(593 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bjzmh0/">March 21, 2024 &nbsp;(420 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bksave/">March 22, 2024 &nbsp;(236 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bll5sr/">March 23, 2024 &nbsp;(242 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bmdq2z/">March 24, 2024 &nbsp;(250 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bn6io6/">March 25, 2024 &nbsp;(413 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bo0lmo/">March 26, 2024 &nbsp;(406 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bour0p/">March 27, 2024 &nbsp;(674 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bpobg6/">March 28, 2024 &nbsp;(363 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bqhysw/">March 29, 2024 &nbsp;(337 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1braopv/">March 30, 2024 &nbsp;(306 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bs2c90/">March 31, 2024 &nbsp;(336 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;April 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bsv48f/">April 01, 2024 &nbsp;(351 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1btqdwj/">April 02, 2024 &nbsp;(353 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1buk90w/">April 03, 2024 &nbsp;(320 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bveuv9/">April 04, 2024 &nbsp;(235 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bw9oqm/">April 05, 2024 &nbsp;(257 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bx39o4/">April 06, 2024 &nbsp;(152 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bxw498/">April 07, 2024 &nbsp;(135 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bypiin/">April 08, 2024 &nbsp;(368 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1bzjwc2/">April 09, 2024 &nbsp;(307 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c0dgy2/">April 10, 2024 &nbsp;(329 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c16oqe/">April 11, 2024 &nbsp;(333 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c20q6p/">April 12, 2024 &nbsp;(377 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c2txwt/">April 13, 2024 &nbsp;(266 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c3lh3q/">April 14, 2024 &nbsp;(155 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c4dy78/">April 15, 2024 &nbsp;(243 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c57t4z/">April 16, 2024 &nbsp;(285 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c61fv6/">April 17, 2024 &nbsp;(394 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c6v2o5/">April 18, 2024 &nbsp;(228 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c7okhx/">April 19, 2024 &nbsp;(337 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c8hqbi/">April 20, 2024 &nbsp;(184 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1c99qz0/">April 21, 2024 &nbsp;(206 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ca2coe/">April 22, 2024 &nbsp;(248 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cawa14/">April 23, 2024 &nbsp;(357 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cbpygi/">April 24, 2024 &nbsp;(327 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ccjko5/">April 25, 2024 &nbsp;(390 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cdcy19/">April 26, 2024 &nbsp;(259 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ce6bam/">April 27, 2024 &nbsp;(258 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ceybho/">April 28, 2024 &nbsp;(257 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cfqsz4/">April 29, 2024 &nbsp;(523 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cgkmut/">April 30, 2024 &nbsp;(431 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;May 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1chdtev/">May 01, 2024 &nbsp;(279 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ci7az9/">May 02, 2024 &nbsp;(207 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cj0i2a/">May 03, 2024 &nbsp;(326 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cjsgqr/">May 04, 2024 &nbsp;(231 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ckjkf6/">May 05, 2024 &nbsp;(164 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1claz43/">May 06, 2024 &nbsp;(335 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cm3wej/">May 07, 2024 &nbsp;(232 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cmwhiy/">May 08, 2024 &nbsp;(343 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cnp6qx/">May 09, 2024 &nbsp;(347 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cohjve/">May 10, 2024 &nbsp;(286 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cp9ldj/">May 11, 2024 &nbsp;(156 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cq04yl/">May 12, 2024 &nbsp;(160 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cqr9e8/">May 13, 2024 &nbsp;(257 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1crk4ou/">May 14, 2024 &nbsp;(337 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cscw1a/">May 15, 2024 &nbsp;(369 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ct57il/">May 16, 2024 &nbsp;(381 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ctx7h5/">May 17, 2024 &nbsp;(218 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cupmmt/">May 18, 2024 &nbsp;(169 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cvghqb/">May 19, 2024 &nbsp;(141 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cw7lio/">May 20, 2024 &nbsp;(852 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cwzy5i/">May 21, 2024 &nbsp;(681 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cxsana/">May 22, 2024 &nbsp;(631 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1cyksus/">May 23, 2024 &nbsp;(1597 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1czcy7e/">May 24, 2024 &nbsp;(434 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d04f4i/">May 25, 2024 &nbsp;(254 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d0u05z/">May 26, 2024 &nbsp;(383 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d1jvid/">May 27, 2024 &nbsp;(380 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d2bjkm/">May 28, 2024 &nbsp;(338 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d348qt/">May 29, 2024 &nbsp;(299 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d3w6lh/">May 30, 2024 &nbsp;(325 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d4nq7l/">May 31, 2024 &nbsp;(284 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;June 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d5fcr3/">June 01, 2024 &nbsp;(164 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d65oxr/">June 02, 2024 &nbsp;(194 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d6wlt8/">June 03, 2024 &nbsp;(209 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d7p4e6/">June 04, 2024 &nbsp;(306 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d8huxx/">June 05, 2024 &nbsp;(464 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1d9ab4c/">June 06, 2024 &nbsp;(340 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1da2nhh/">June 07, 2024 &nbsp;(248 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dav3w9/">June 08, 2024 &nbsp;(120 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dblvjg/">June 09, 2024 &nbsp;(177 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dcdm7q/">June 10, 2024 &nbsp;(183 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dd65dm/">June 11, 2024 &nbsp;(522 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ddymob/">June 12, 2024 &nbsp;(244 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1deqzov/">June 13, 2024 &nbsp;(234 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dfiz4n/">June 14, 2024 &nbsp;(278 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dgacad/">June 15, 2024 &nbsp;(171 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dh06hm/">June 16, 2024 &nbsp;(155 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dhq7bj/">June 17, 2024 &nbsp;(313 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1diimbq/">June 18, 2024 &nbsp;(249 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1djb287/">June 19, 2024 &nbsp;(294 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dk3kzx/">June 20, 2024 &nbsp;(267 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dkvydm/">June 21, 2024 &nbsp;(184 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dlnxhn/">June 22, 2024 &nbsp;(135 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dmej84/">June 23, 2024 &nbsp;(86 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dn5jyx/">June 24, 2024 &nbsp;(343 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dnxzmo/">June 25, 2024 &nbsp;(193 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1doqi9m/">June 26, 2024 &nbsp;(204 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dpj7ve/">June 27, 2024 &nbsp;(230 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dqbnti/">June 28, 2024 &nbsp;(204 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dr3hwv/">June 29, 2024 &nbsp;(73 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1drtvtk/">June 30, 2024 &nbsp;(104 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;July 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dsktd4/">July 01, 2024 &nbsp;(130 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dtdqvc/">July 02, 2024 &nbsp;(151 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1du681u/">July 03, 2024 &nbsp;(233 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1duyoim/">July 04, 2024 &nbsp;(240 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dvpzvb/">July 05, 2024 &nbsp;(311 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dwhu31/">July 06, 2024 &nbsp;(159 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dx8nwu/">July 07, 2024 &nbsp;(236 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dy0lbc/">July 08, 2024 &nbsp;(216 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dyu2vs/">July 09, 2024 &nbsp;(170 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1dzng6z/">July 10, 2024 &nbsp;(244 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e0gtdv/">July 11, 2024 &nbsp;(139 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e199nr/">July 12, 2024 &nbsp;(102 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e228zf/">July 13, 2024 &nbsp;(84 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e2u37g/">July 14, 2024 &nbsp;(106 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e3mhq2/">July 15, 2024 &nbsp;(290 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e4g8sf/">July 16, 2024 &nbsp;(198 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e59tk5/">July 17, 2024 &nbsp;(222 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e639w5/">July 18, 2024 &nbsp;(204 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e6vo0l/">July 19, 2024 &nbsp;(218 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e7nt2y/">July 20, 2024 &nbsp;(218 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e8ely9/">July 21, 2024 &nbsp;(190 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e960uq/">July 22, 2024 &nbsp;(248 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1e9zgce/">July 23, 2024 &nbsp;(634 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eat246/">July 24, 2024 &nbsp;(404 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ebmjo4/">July 25, 2024 &nbsp;(419 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ecfslx/">July 26, 2024 &nbsp;(229 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ed8f13/">July 27, 2024 &nbsp;(149 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1edzplc/">July 28, 2024 &nbsp;(153 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eer8s9/">July 29, 2024 &nbsp;(182 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1efl096/">July 30, 2024 &nbsp;(160 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1egeu6r/">July 31, 2024 &nbsp;(188 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;August 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eh8e2q/">August 01, 2024 &nbsp;(176 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ei1pba/">August 02, 2024 &nbsp;(261 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eiv2vm/">August 03, 2024 &nbsp;(183 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ejnbk4/">August 04, 2024 &nbsp;(445 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ekfjb6/">August 05, 2024 &nbsp;(572 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1el99as/">August 06, 2024 &nbsp;(227 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1em3ca0/">August 07, 2024 &nbsp;(562 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1emxgi7/">August 08, 2024 &nbsp;(309 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1enrae5/">August 09, 2024 &nbsp;(181 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eokvya/">August 10, 2024 &nbsp;(87 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1epcojy/">August 11, 2024 &nbsp;(123 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eq57le/">August 12, 2024 &nbsp;(175 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eqzi34/">August 13, 2024 &nbsp;(242 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ert4tl/">August 14, 2024 &nbsp;(167 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1esmtac/">August 15, 2024 &nbsp;(254 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1etgdqq/">August 16, 2024 &nbsp;(152 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eu9s49/">August 17, 2024 &nbsp;(94 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ev1b2x/">August 18, 2024 &nbsp;(68 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1evtl8k/">August 19, 2024 &nbsp;(141 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ewn8dw/">August 20, 2024 &nbsp;(272 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1exh5g5/">August 21, 2024 &nbsp;(195 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1eyb1rd/">August 22, 2024 &nbsp;(157 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ez4fxr/">August 23, 2024 &nbsp;(253 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ezxfho/">August 24, 2024 &nbsp;(236 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f0opjz/">August 25, 2024 &nbsp;(87 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f1g6p2/">August 26, 2024 &nbsp;(164 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f29003/">August 27, 2024 &nbsp;(321 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f31zal/">August 28, 2024 &nbsp;(284 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f3uche/">August 29, 2024 &nbsp;(205 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f4n4q0/">August 30, 2024 &nbsp;(176 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f5fiqc/">August 31, 2024 &nbsp;(73 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;September 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f66n0f/">September 01, 2024 &nbsp;(112 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f6yl0k/">September 02, 2024 &nbsp;(169 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f7rrbo/">September 03, 2024 &nbsp;(239 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f8l3t3/">September 04, 2024 &nbsp;(203 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1f9ef5k/">September 05, 2024 &nbsp;(231 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fa76dn/">September 06, 2024 &nbsp;(386 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fazb7o/">September 07, 2024 &nbsp;(164 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fbq2nu/">September 08, 2024 &nbsp;(173 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fcho6q/">September 09, 2024 &nbsp;(251 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fda31e/">September 10, 2024 &nbsp;(168 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fe29xd/">September 11, 2024 &nbsp;(167 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1feun79/">September 12, 2024 &nbsp;(228 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ffmt2l/">September 13, 2024 &nbsp;(129 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fgelps/">September 14, 2024 &nbsp;(94 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fh4v1q/">September 15, 2024 &nbsp;(236 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fhwp53/">September 16, 2024 &nbsp;(188 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fiqhc6/">September 17, 2024 &nbsp;(187 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fjkzpm/">September 18, 2024 &nbsp;(276 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fkd3pr/">September 19, 2024 &nbsp;(285 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fl4c68/">September 20, 2024 &nbsp;(282 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1flvgzu/">September 21, 2024 &nbsp;(155 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fmlkae/">September 22, 2024 &nbsp;(78 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fncsy5/">September 23, 2024 &nbsp;(199 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fo4r11/">September 24, 2024 &nbsp;(212 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fowp6i/">September 25, 2024 &nbsp;(237 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fpojgj/">September 26, 2024 &nbsp;(251 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fqg5x4/">September 27, 2024 &nbsp;(238 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fr6w8s/">September 28, 2024 &nbsp;(89 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1frwuf6/">September 29, 2024 &nbsp;(89 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fsnv17/">September 30, 2024 &nbsp;(187 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;October 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ftg8jb/">October 01, 2024 &nbsp;(156 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fu8i74/">October 02, 2024 &nbsp;(224 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fv071m/">October 03, 2024 &nbsp;(276 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fvrhxr/">October 04, 2024 &nbsp;(105 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fwivoc/">October 05, 2024 &nbsp;(106 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fx9170/">October 06, 2024 &nbsp;(77 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fxzz7t/">October 07, 2024 &nbsp;(188 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fys4ny/">October 08, 2024 &nbsp;(184 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1fzjust/">October 09, 2024 &nbsp;(110 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g0bcb1/">October 10, 2024 &nbsp;(187 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g127sk/">October 11, 2024 &nbsp;(238 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g1suyn/">October 12, 2024 &nbsp;(136 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g2ial1/">October 13, 2024 &nbsp;(109 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g38jps/">October 14, 2024 &nbsp;(238 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g405r7/">October 15, 2024 &nbsp;(228 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g4roxi/">October 16, 2024 &nbsp;(250 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g5j8g6/">October 17, 2024 &nbsp;(287 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g6ag98/">October 18, 2024 &nbsp;(153 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g71lyc/">October 19, 2024 &nbsp;(156 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g7rawa/">October 20, 2024 &nbsp;(154 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g8i1bx/">October 21, 2024 &nbsp;(222 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1g9aee7/">October 22, 2024 &nbsp;(317 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ga2kk9/">October 23, 2024 &nbsp;(217 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gaux5i/">October 24, 2024 &nbsp;(339 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gbml3v/">October 25, 2024 &nbsp;(246 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gcdmiv/">October 26, 2024 &nbsp;(148 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gd4es8/">October 27, 2024 &nbsp;(84 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gdv8ez/">October 28, 2024 &nbsp;(220 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gent1b/">October 29, 2024 &nbsp;(314 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gffucb/">October 30, 2024 &nbsp;(309 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gg7smg/">October 31, 2024 &nbsp;(245 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;November 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ggyuhz/">November 01, 2024 &nbsp;(198 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ghq1qr/">November 02, 2024 &nbsp;(97 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gigfh8/">November 03, 2024 &nbsp;(82 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gj7n46/">November 04, 2024 &nbsp;(155 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gk03k8/">November 05, 2024 &nbsp;(196 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gkrnmn/">November 06, 2024 &nbsp;(698 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gljtif/">November 07, 2024 &nbsp;(360 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gmbv28/">November 08, 2024 &nbsp;(287 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gn3k7p/">November 09, 2024 &nbsp;(449 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gnu2i8/">November 10, 2024 &nbsp;(390 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1golgs1/">November 11, 2024 &nbsp;(543 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gpe52f/">November 12, 2024 &nbsp;(330 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gq6ahm/">November 13, 2024 &nbsp;(644 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gqybdj/">November 14, 2024 &nbsp;(348 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1grps72/">November 15, 2024 &nbsp;(419 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gsgu9w/">November 16, 2024 &nbsp;(296 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gt73qz/">November 17, 2024 &nbsp;(434 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gty62j/">November 18, 2024 &nbsp;(338 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1guqj19/">November 19, 2024 &nbsp;(470 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gviwdw/">November 20, 2024 &nbsp;(634 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gw9gyb/">November 21, 2024 &nbsp;(633 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gx14zh/">November 22, 2024 &nbsp;(494 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gxswpb/">November 23, 2024 &nbsp;(365 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gyk72r/">November 24, 2024 &nbsp;(222 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1gzc4yp/">November 25, 2024 &nbsp;(448 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h0513t/">November 26, 2024 &nbsp;(218 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h0xkvx/">November 27, 2024 &nbsp;(600 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h1pbw9/">November 28, 2024 &nbsp;(289 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h2f5g1/">November 29, 2024 &nbsp;(254 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h3623z/">November 30, 2024 &nbsp;(259 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;December 2024</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h3wpf4/">December 01, 2024 &nbsp;(321 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h4ob2e/">December 02, 2024 &nbsp;(434 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h5gs1z/">December 03, 2024 &nbsp;(474 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h69auf/">December 04, 2024 &nbsp;(584 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h72g4u/">December 05, 2024 &nbsp;(623 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h7upd0/">December 06, 2024 &nbsp;(814 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h8m296/">December 07, 2024 &nbsp;(187 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1h9cc2u/">December 08, 2024 &nbsp;(181 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1ha36r5/">December 09, 2024 &nbsp;(418 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hav6kf/">December 10, 2024 &nbsp;(301 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hbmz67/">December 11, 2024 &nbsp;(344 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hcem8v/">December 12, 2024 &nbsp;(455 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hd5v9m/">December 13, 2024 &nbsp;(276 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hdwg79/">December 14, 2024 &nbsp;(231 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hembku/">December 15, 2024 &nbsp;(269 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hfco5b/">December 16, 2024 &nbsp;(395 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hg47a5/">December 17, 2024 &nbsp;(379 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hgv892/">December 18, 2024 &nbsp;(382 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hhmbc0/">December 19, 2024 &nbsp;(455 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hidcgv/">December 20, 2024 &nbsp;(462 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hie9hh/">December 20, 2024 &nbsp;(140 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hj4iae/">December 21, 2024 &nbsp;(36 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hj3mq7/">December 21, 2024 &nbsp;(96 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hjsjxq/">December 22, 2024 &nbsp;(131 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hjtdsk/">December 22, 2024 &nbsp;(29 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hkic01/">December 23, 2024 &nbsp;(134 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hkhgfo/">December 23, 2024 &nbsp;(147 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hl77fx/">December 24, 2024 &nbsp;(81 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hl83c1/">December 24, 2024 &nbsp;(109 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hluyp6/">December 25, 2024 &nbsp;(76 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hlvrvj/">December 25, 2024 &nbsp;(53 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hmj3dc/">December 26, 2024 &nbsp;(120 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hmi8g5/">December 26, 2024 &nbsp;(64 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hn8f1y/">December 27, 2024 &nbsp;(90 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hn9bv6/">December 27, 2024 &nbsp;(114 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1ho0ad0/">December 28, 2024 &nbsp;(122 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hnzdk8/">December 28, 2024 &nbsp;(47 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hoqjln/">December 29, 2024 &nbsp;(87 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hopm1d/">December 29, 2024 &nbsp;(75 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hphjd1/">December 30, 2024 &nbsp;(140 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hpgla2/">December 30, 2024 &nbsp;(89 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1hq8bu0/">December 31, 2024 &nbsp;(445 comments)</a></li>
      <li><a href="https://reddit.com/r/ethereum/comments/1hq99kz/">December 31, 2024 &nbsp;(145 comments)</a></li>
    </ul>
  </details>
</details>

<!-- 2023 -->
<details>
  <summary>&nbsp;2023</summary>
  <details>
    <summary>&nbsp;January 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/100d6c2/">January 01, 2023 &nbsp;(273 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1014ypw/">January 02, 2023 &nbsp;(402 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/101zwim/">January 03, 2023 &nbsp;(447 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/102vnu4/">January 04, 2023 &nbsp;(382 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/103r9ly/">January 05, 2023 &nbsp;(387 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/104mg1j/">January 06, 2023 &nbsp;(311 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/105hh6b/">January 07, 2023 &nbsp;(308 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/106bh8s/">January 08, 2023 &nbsp;(382 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1076f4p/">January 09, 2023 &nbsp;(534 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10827ir/">January 10, 2023 &nbsp;(432 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/108x76j/">January 11, 2023 &nbsp;(643 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/109rzd5/">January 12, 2023 &nbsp;(598 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10amvdl/">January 13, 2023 &nbsp;(659 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10bh29t/">January 14, 2023 &nbsp;(487 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10cc78w/">January 15, 2023 &nbsp;(504 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10d6prc/">January 16, 2023 &nbsp;(438 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10e4kij/">January 17, 2023 &nbsp;(411 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10ezr5l/">January 18, 2023 &nbsp;(565 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10fu4px/">January 19, 2023 &nbsp;(377 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10gp4if/">January 20, 2023 &nbsp;(619 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10hk7qe/">January 21, 2023 &nbsp;(464 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10icjgc/">January 22, 2023 &nbsp;(345 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10j5dkj/">January 23, 2023 &nbsp;(427 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10jyo68/">January 24, 2023 &nbsp;(486 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10krmxu/">January 25, 2023 &nbsp;(397 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10lkzyb/">January 26, 2023 &nbsp;(282 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10mdp58/">January 27, 2023 &nbsp;(306 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10n7qyq/">January 28, 2023 &nbsp;(337 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10o0h5d/">January 29, 2023 &nbsp;(414 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10oudh1/">January 30, 2023 &nbsp;(349 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10pqbiw/">January 31, 2023 &nbsp;(514 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;February 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/10qm414/">February 01, 2023 &nbsp;(467 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10rigcl/">February 02, 2023 &nbsp;(573 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10scsic/">February 03, 2023 &nbsp;(436 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10t6kdg/">February 04, 2023 &nbsp;(307 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10u5d4l/">February 05, 2023 &nbsp;(263 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10uz7x0/">February 06, 2023 &nbsp;(344 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10vuce8/">February 07, 2023 &nbsp;(380 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10woz0p/">February 08, 2023 &nbsp;(527 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10xn2mv/">February 09, 2023 &nbsp;(974 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10yhsb2/">February 10, 2023 &nbsp;(507 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/10zdqvt/">February 11, 2023 &nbsp;(308 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1108k4a/">February 12, 2023 &nbsp;(275 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1111020/">February 13, 2023 &nbsp;(486 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/111vdwx/">February 14, 2023 &nbsp;(649 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/112qy29/">February 15, 2023 &nbsp;(489 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/113jhtv/">February 16, 2023 &nbsp;(561 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/114c6on/">February 17, 2023 &nbsp;(542 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1158cdi/">February 18, 2023 &nbsp;(285 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11632qy/">February 19, 2023 &nbsp;(312 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/116z82t/">February 20, 2023 &nbsp;(342 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/117w2io/">February 21, 2023 &nbsp;(286 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/118qid5/">February 22, 2023 &nbsp;(393 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/119q5kg/">February 23, 2023 &nbsp;(494 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11ak2qc/">February 24, 2023 &nbsp;(425 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11bdlrh/">February 25, 2023 &nbsp;(283 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11c6vcs/">February 26, 2023 &nbsp;(271 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11d4bra/">February 27, 2023 &nbsp;(365 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11dyi3r/">February 28, 2023 &nbsp;(301 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;March 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/11evx0c/">March 01, 2023 &nbsp;(457 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11fuqpf/">March 02, 2023 &nbsp;(324 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11gsztq/">March 03, 2023 &nbsp;(333 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11hraxm/">March 04, 2023 &nbsp;(180 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11ip8sx/">March 05, 2023 &nbsp;(242 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11jq6y5/">March 06, 2023 &nbsp;(239 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11kqzjp/">March 07, 2023 &nbsp;(298 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11lo2v3/">March 08, 2023 &nbsp;(291 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11mkewq/">March 09, 2023 &nbsp;(488 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11ngir4/">March 10, 2023 &nbsp;(756 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11ocbsl/">March 11, 2023 &nbsp;(795 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11p6xk6/">March 12, 2023 &nbsp;(528 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11q1nrm/">March 13, 2023 &nbsp;(936 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11qy7me/">March 14, 2023 &nbsp;(576 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11rnp2q/">March 15, 2023 &nbsp;(516 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11slqjw/">March 16, 2023 &nbsp;(870 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11tipbq/">March 17, 2023 &nbsp;(926 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11ufzg6/">March 18, 2023 &nbsp;(487 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11vd15b/">March 19, 2023 &nbsp;(452 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11waa98/">March 20, 2023 &nbsp;(664 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11x8e2l/">March 21, 2023 &nbsp;(521 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11y8xk3/">March 22, 2023 &nbsp;(668 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/11zaqp2/">March 23, 2023 &nbsp;(1295 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/120axdk/">March 24, 2023 &nbsp;(721 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/121cklf/">March 25, 2023 &nbsp;(370 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/122blya/">March 26, 2023 &nbsp;(307 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/123c10y/">March 27, 2023 &nbsp;(462 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/124dk9m/">March 28, 2023 &nbsp;(549 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/125dn51/">March 29, 2023 &nbsp;(500 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/126c8nf/">March 30, 2023 &nbsp;(469 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/127app5/">March 31, 2023 &nbsp;(480 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;April 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/128bsd0/">April 01, 2023 &nbsp;(364 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/129amhp/">April 02, 2023 &nbsp;(314 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12aa0sa/">April 03, 2023 &nbsp;(513 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12b9hj4/">April 04, 2023 &nbsp;(572 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12c90ok/">April 05, 2023 &nbsp;(555 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12d9ndu/">April 06, 2023 &nbsp;(406 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12eagbz/">April 07, 2023 &nbsp;(359 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12fc4ge/">April 08, 2023 &nbsp;(275 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12g9dz5/">April 09, 2023 &nbsp;(259 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12h7qgo/">April 10, 2023 &nbsp;(478 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12i920r/">April 11, 2023 &nbsp;(605 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12jan7l/">April 12, 2023 &nbsp;(1386 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12kcm3z/">April 13, 2023 &nbsp;(1151 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12lkn8x/">April 14, 2023 &nbsp;(783 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12mqnlc/">April 15, 2023 &nbsp;(388 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12nw0o0/">April 16, 2023 &nbsp;(440 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12p2uhe/">April 17, 2023 &nbsp;(592 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12qb6uw/">April 18, 2023 &nbsp;(831 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12rhig4/">April 19, 2023 &nbsp;(671 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12smokw/">April 20, 2023 &nbsp;(354 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12tqxpv/">April 21, 2023 &nbsp;(337 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12uv9kn/">April 22, 2023 &nbsp;(270 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12vwbun/">April 23, 2023 &nbsp;(260 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12x3uzq/">April 24, 2023 &nbsp;(392 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12y8q1c/">April 25, 2023 &nbsp;(400 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/12z6zsm/">April 26, 2023 &nbsp;(460 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/130aejt/">April 27, 2023 &nbsp;(393 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/131i3ej/">April 28, 2023 &nbsp;(322 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/132jpw8/">April 29, 2023 &nbsp;(454 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/133g9bo/">April 30, 2023 &nbsp;(345 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;May 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/134d3x2/">May 01, 2023 &nbsp;(288 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/135bq9m/">May 02, 2023 &nbsp;(337 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/136avsi/">May 03, 2023 &nbsp;(527 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/137aiu4/">May 04, 2023 &nbsp;(476 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/138b9bt/">May 05, 2023 &nbsp;(478 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/139cnll/">May 06, 2023 &nbsp;(358 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13ademz/">May 07, 2023 &nbsp;(310 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13behyv/">May 08, 2023 &nbsp;(462 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13cfzjx/">May 09, 2023 &nbsp;(442 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13dgrhp/">May 10, 2023 &nbsp;(340 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13edhzt/">May 11, 2023 &nbsp;(345 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13fbc6v/">May 12, 2023 &nbsp;(379 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13g7s03/">May 13, 2023 &nbsp;(189 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13h32x6/">May 14, 2023 &nbsp;(278 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13hy6ue/">May 15, 2023 &nbsp;(372 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13ivi8v/">May 16, 2023 &nbsp;(1055 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13jryjf/">May 17, 2023 &nbsp;(680 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13kozpl/">May 18, 2023 &nbsp;(372 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13lliuv/">May 19, 2023 &nbsp;(248 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13migau/">May 20, 2023 &nbsp;(204 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13njevl/">May 21, 2023 &nbsp;(230 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13ogyzj/">May 22, 2023 &nbsp;(333 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13pejil/">May 23, 2023 &nbsp;(258 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13qbpch/">May 24, 2023 &nbsp;(264 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13r8eom/">May 25, 2023 &nbsp;(216 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13s3pp7/">May 26, 2023 &nbsp;(308 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13sygtc/">May 27, 2023 &nbsp;(241 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13trvpr/">May 28, 2023 &nbsp;(225 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13uldb1/">May 29, 2023 &nbsp;(147 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13vh1j4/">May 30, 2023 &nbsp;(263 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13wcu4w/">May 31, 2023 &nbsp;(321 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;June 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/13x8njw/">June 01, 2023 &nbsp;(499 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13y3hr6/">June 02, 2023 &nbsp;(344 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/13z1f41/">June 03, 2023 &nbsp;(280 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1401prr/">June 04, 2023 &nbsp;(238 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1412u9x/">June 05, 2023 &nbsp;(530 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1424agt/">June 06, 2023 &nbsp;(524 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1433ugu/">June 07, 2023 &nbsp;(413 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/143ztf8/">June 08, 2023 &nbsp;(320 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/144vs24/">June 09, 2023 &nbsp;(392 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/145qzkz/">June 10, 2023 &nbsp;(348 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/146kydb/">June 11, 2023 &nbsp;(269 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/147fedq/">June 12, 2023 &nbsp;(9 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1486xqz/">June 13, 2023 &nbsp;(26 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/148yyad/">June 14, 2023 &nbsp;(450 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/149t8gd/">June 15, 2023 &nbsp;(380 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14anky9/">June 16, 2023 &nbsp;(280 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14bhuxo/">June 17, 2023 &nbsp;(193 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14cbhdh/">June 18, 2023 &nbsp;(136 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14d4z2j/">June 19, 2023 &nbsp;(206 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14e1fzr/">June 20, 2023 &nbsp;(288 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14exz6d/">June 21, 2023 &nbsp;(372 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14ftwtr/">June 22, 2023 &nbsp;(362 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14gpcpl/">June 23, 2023 &nbsp;(274 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14hjvmz/">June 24, 2023 &nbsp;(140 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14idb8o/">June 25, 2023 &nbsp;(194 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14j7oa4/">June 26, 2023 &nbsp;(172 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14k3xkf/">June 27, 2023 &nbsp;(264 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14l05iz/">June 28, 2023 &nbsp;(248 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14lvn8p/">June 29, 2023 &nbsp;(339 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14mqtwd/">June 30, 2023 &nbsp;(340 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;July 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/14nm41j/">July 01, 2023 &nbsp;(170 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14ofheb/">July 02, 2023 &nbsp;(170 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14p9enj/">July 03, 2023 &nbsp;(256 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14q5dmj/">July 04, 2023 &nbsp;(240 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14r0ocb/">July 05, 2023 &nbsp;(218 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14ryifk/">July 06, 2023 &nbsp;(178 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14sx3ji/">July 07, 2023 &nbsp;(216 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14tuakx/">July 08, 2023 &nbsp;(180 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14uphdc/">July 09, 2023 &nbsp;(108 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14vk91l/">July 10, 2023 &nbsp;(205 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14whcr5/">July 11, 2023 &nbsp;(154 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14xehxp/">July 12, 2023 &nbsp;(185 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14yb895/">July 13, 2023 &nbsp;(416 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/14z6vmh/">July 14, 2023 &nbsp;(318 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1502itd/">July 15, 2023 &nbsp;(177 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/150x3om/">July 16, 2023 &nbsp;(253 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/151s5nw/">July 17, 2023 &nbsp;(220 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/152ossl/">July 18, 2023 &nbsp;(262 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/153l7fp/">July 19, 2023 &nbsp;(265 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/154hewp/">July 20, 2023 &nbsp;(206 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/155dxre/">July 21, 2023 &nbsp;(243 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/156an5v/">July 22, 2023 &nbsp;(105 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1575gjm/">July 23, 2023 &nbsp;(135 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1580pwg/">July 24, 2023 &nbsp;(247 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/158y8lm/">July 25, 2023 &nbsp;(223 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/159w1cr/">July 26, 2023 &nbsp;(230 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15ase4i/">July 27, 2023 &nbsp;(364 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15bntnh/">July 28, 2023 &nbsp;(233 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15cjdhc/">July 29, 2023 &nbsp;(117 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15dcqqy/">July 30, 2023 &nbsp;(196 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15e6kzl/">July 31, 2023 &nbsp;(307 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;August 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/15f2oxj/">August 01, 2023 &nbsp;(299 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15fzcv4/">August 02, 2023 &nbsp;(135 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15guiww/">August 03, 2023 &nbsp;(264 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15hqkud/">August 04, 2023 &nbsp;(155 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15imfx8/">August 05, 2023 &nbsp;(89 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15jgsfr/">August 06, 2023 &nbsp;(99 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15kauxp/">August 07, 2023 &nbsp;(253 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15l83h6/">August 08, 2023 &nbsp;(224 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15m5eq1/">August 09, 2023 &nbsp;(193 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15n2m0t/">August 10, 2023 &nbsp;(274 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15nz9zj/">August 11, 2023 &nbsp;(167 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15ovax3/">August 12, 2023 &nbsp;(145 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15ppv3o/">August 13, 2023 &nbsp;(129 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15qkvqf/">August 14, 2023 &nbsp;(254 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15rirbm/">August 15, 2023 &nbsp;(208 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15sg07d/">August 16, 2023 &nbsp;(311 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15tdehc/">August 17, 2023 &nbsp;(535 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15uartw/">August 18, 2023 &nbsp;(256 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15v6qz8/">August 19, 2023 &nbsp;(125 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15w1z93/">August 20, 2023 &nbsp;(159 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15wxpta/">August 21, 2023 &nbsp;(185 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15xvfqk/">August 22, 2023 &nbsp;(188 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15yts52/">August 23, 2023 &nbsp;(198 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/15zrzr8/">August 24, 2023 &nbsp;(236 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/160phdq/">August 25, 2023 &nbsp;(177 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/161lowk/">August 26, 2023 &nbsp;(189 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/162h6a2/">August 27, 2023 &nbsp;(169 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/163cqkk/">August 28, 2023 &nbsp;(150 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1648z88/">August 29, 2023 &nbsp;(267 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1655c71/">August 30, 2023 &nbsp;(182 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1661ki5/">August 31, 2023 &nbsp;(211 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;September 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/166xsuy/">September 01, 2023 &nbsp;(256 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/167tggf/">September 02, 2023 &nbsp;(102 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/168nzxs/">September 03, 2023 &nbsp;(125 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/169imcm/">September 04, 2023 &nbsp;(161 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16aesof/">September 05, 2023 &nbsp;(213 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16bb42v/">September 06, 2023 &nbsp;(339 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16c6vpw/">September 07, 2023 &nbsp;(172 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16d18dh/">September 08, 2023 &nbsp;(172 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16dwu2k/">September 09, 2023 &nbsp;(82 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16eramm/">September 10, 2023 &nbsp;(101 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16fmfto/">September 11, 2023 &nbsp;(230 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16gi7gg/">September 12, 2023 &nbsp;(191 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16hdwk1/">September 13, 2023 &nbsp;(219 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16i99gu/">September 14, 2023 &nbsp;(198 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16j45ua/">September 15, 2023 &nbsp;(169 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16jyqtv/">September 16, 2023 &nbsp;(100 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16krxzo/">September 17, 2023 &nbsp;(110 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16lmall/">September 18, 2023 &nbsp;(212 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16mhwki/">September 19, 2023 &nbsp;(219 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16ncizo/">September 20, 2023 &nbsp;(154 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16o6wvt/">September 21, 2023 &nbsp;(286 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16p1i17/">September 22, 2023 &nbsp;(101 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16pvjq0/">September 23, 2023 &nbsp;(125 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16qowk7/">September 24, 2023 &nbsp;(74 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16riyuo/">September 25, 2023 &nbsp;(128 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16seir4/">September 26, 2023 &nbsp;(138 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16tbda8/">September 27, 2023 &nbsp;(234 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16u6ws6/">September 28, 2023 &nbsp;(230 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16v2i2p/">September 29, 2023 &nbsp;(202 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16vy0ih/">September 30, 2023 &nbsp;(104 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;October 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/16ws5iy/">October 01, 2023 &nbsp;(145 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16xno81/">October 02, 2023 &nbsp;(202 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16yj1h2/">October 03, 2023 &nbsp;(140 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/16ze8g1/">October 04, 2023 &nbsp;(201 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17098wb/">October 05, 2023 &nbsp;(362 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1713or9/">October 06, 2023 &nbsp;(253 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/171xu2i/">October 07, 2023 &nbsp;(80 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/172qnoh/">October 08, 2023 &nbsp;(100 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/173jl7e/">October 09, 2023 &nbsp;(188 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/174d0di/">October 10, 2023 &nbsp;(213 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1756266/">October 11, 2023 &nbsp;(218 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/175ysyn/">October 12, 2023 &nbsp;(359 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/176qwfi/">October 13, 2023 &nbsp;(207 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/177hut9/">October 14, 2023 &nbsp;(213 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1788062/">October 15, 2023 &nbsp;(91 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/178y9gp/">October 16, 2023 &nbsp;(210 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/179qkqi/">October 17, 2023 &nbsp;(212 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17aimuj/">October 18, 2023 &nbsp;(211 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17bb5od/">October 19, 2023 &nbsp;(195 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17c390i/">October 20, 2023 &nbsp;(208 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17cuvcq/">October 21, 2023 &nbsp;(139 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17dlmmp/">October 22, 2023 &nbsp;(129 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17ecnkq/">October 23, 2023 &nbsp;(508 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17f4y90/">October 24, 2023 &nbsp;(454 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17fx5jb/">October 25, 2023 &nbsp;(271 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17gov0s/">October 26, 2023 &nbsp;(318 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17hfyq2/">October 27, 2023 &nbsp;(219 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17i6g3p/">October 28, 2023 &nbsp;(186 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17iwjjx/">October 29, 2023 &nbsp;(168 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17jmpyt/">October 30, 2023 &nbsp;(212 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17keaci/">October 31, 2023 &nbsp;(360 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;November 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/17l5kd9/">November 01, 2023 &nbsp;(322 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17lwxn0/">November 02, 2023 &nbsp;(287 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17moc9h/">November 03, 2023 &nbsp;(215 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17nf8et/">November 04, 2023 &nbsp;(180 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17o5md4/">November 05, 2023 &nbsp;(269 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17ow6kv/">November 06, 2023 &nbsp;(187 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17pnrin/">November 07, 2023 &nbsp;(294 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17qf8oj/">November 08, 2023 &nbsp;(295 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17r6fn6/">November 09, 2023 &nbsp;(784 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17rxlo5/">November 10, 2023 &nbsp;(381 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17so8sk/">November 11, 2023 &nbsp;(165 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17tdxnc/">November 12, 2023 &nbsp;(158 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17u49k4/">November 13, 2023 &nbsp;(222 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17uvruy/">November 14, 2023 &nbsp;(282 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17vn3bx/">November 15, 2023 &nbsp;(364 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17wfnq9/">November 16, 2023 &nbsp;(364 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17x8g4p/">November 17, 2023 &nbsp;(314 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17xzw1y/">November 18, 2023 &nbsp;(157 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17yqeuw/">November 19, 2023 &nbsp;(209 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/17zhsdo/">November 20, 2023 &nbsp;(373 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/180a3d0/">November 21, 2023 &nbsp;(326 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/1812a9r/">November 22, 2023 &nbsp;(400 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/181udkk/">November 23, 2023 &nbsp;(256 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/182l6a4/">November 24, 2023 &nbsp;(298 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/183d0jg/">November 25, 2023 &nbsp;(235 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18441na/">November 26, 2023 &nbsp;(260 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/184w10b/">November 27, 2023 &nbsp;(268 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/185p2wo/">November 28, 2023 &nbsp;(232 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/186ihjr/">November 29, 2023 &nbsp;(331 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/187bfcu/">November 30, 2023 &nbsp;(304 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;December 2023</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/1884mjc/">December 01, 2023 &nbsp;(236 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/188x4q0/">December 02, 2023 &nbsp;(374 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/189n2j6/">December 03, 2023 &nbsp;(296 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18adty2/">December 04, 2023 &nbsp;(379 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18b5cgi/">December 05, 2023 &nbsp;(472 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18bxesk/">December 06, 2023 &nbsp;(427 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18cp088/">December 07, 2023 &nbsp;(505 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18dg7y9/">December 08, 2023 &nbsp;(426 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18e6xji/">December 09, 2023 &nbsp;(233 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18ewx8m/">December 10, 2023 &nbsp;(356 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18fnqr1/">December 11, 2023 &nbsp;(237 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18gf4sr/">December 12, 2023 &nbsp;(244 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18ha3pq/">December 13, 2023 &nbsp;(317 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18i1xpa/">December 14, 2023 &nbsp;(387 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18itav8/">December 15, 2023 &nbsp;(331 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18jkos4/">December 16, 2023 &nbsp;(309 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18kamvf/">December 17, 2023 &nbsp;(193 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18l1qbj/">December 18, 2023 &nbsp;(237 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18luu66/">December 19, 2023 &nbsp;(262 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18mnig7/">December 20, 2023 &nbsp;(562 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18nfxvo/">December 21, 2023 &nbsp;(495 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18o7zxl/">December 22, 2023 &nbsp;(451 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18oz4wq/">December 23, 2023 &nbsp;(246 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18poy1s/">December 24, 2023 &nbsp;(245 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18qco7w/">December 25, 2023 &nbsp;(136 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18r1c9q/">December 26, 2023 &nbsp;(193 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18rth8u/">December 27, 2023 &nbsp;(405 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18smom7/">December 28, 2023 &nbsp;(253 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18tfykq/">December 29, 2023 &nbsp;(215 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18u8jft/">December 30, 2023 &nbsp;(140 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/18v0z74/">December 31, 2023 &nbsp;(211 comments)</a></li>
    </ul>
  </details>
</details>

<!-- 2022 -->
<details>
  <summary>&nbsp;2022</summary>
  <details>
    <summary>&nbsp;January 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/rtcxl9/">January 01, 2022 &nbsp;(828 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ru34mk/">January 02, 2022 &nbsp;(688 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ruulob/">January 03, 2022 &nbsp;(765 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rvn86v/">January 04, 2022 &nbsp;(1022 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rwfqzv/">January 05, 2022 &nbsp;(1197 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rx78g4/">January 06, 2022 &nbsp;(1224 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ry0c3b/">January 07, 2022 &nbsp;(1238 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rysxpo/">January 08, 2022 &nbsp;(1069 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rzkwu8/">January 09, 2022 &nbsp;(648 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s0cqgd/">January 10, 2022 &nbsp;(999 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s15tsf/">January 11, 2022 &nbsp;(977 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s1yxv0/">January 12, 2022 &nbsp;(935 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s2s4dk/">January 13, 2022 &nbsp;(945 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s3kzr2/">January 14, 2022 &nbsp;(732 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s4dfx4/">January 15, 2022 &nbsp;(617 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s55358/">January 16, 2022 &nbsp;(609 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s5wm13/">January 17, 2022 &nbsp;(849 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s6qb5y/">January 18, 2022 &nbsp;(942 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s7j59d/">January 19, 2022 &nbsp;(972 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s8btdf/">January 20, 2022 &nbsp;(1424 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s93u0a/">January 21, 2022 &nbsp;(1762 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/s9vnak/">January 22, 2022 &nbsp;(1529 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/samoic/">January 23, 2022 &nbsp;(840 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sbexwx/">January 24, 2022 &nbsp;(1428 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sc6ozb/">January 25, 2022 &nbsp;(1070 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/scywd0/">January 26, 2022 &nbsp;(1295 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sdrepi/">January 27, 2022 &nbsp;(1148 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sejqgi/">January 28, 2022 &nbsp;(970 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sfbh3x/">January 29, 2022 &nbsp;(908 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sg2dio/">January 30, 2022 &nbsp;(856 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sgtyj0/">January 31, 2022 &nbsp;(921 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;February 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/shnot0/">February 01, 2022 &nbsp;(916 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sih4qe/">February 02, 2022 &nbsp;(1040 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sjbld7/">February 03, 2022 &nbsp;(934 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sk5vmt/">February 04, 2022 &nbsp;(1195 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/skzqf0/">February 05, 2022 &nbsp;(717 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/slpdz0/">February 06, 2022 &nbsp;(907 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/smiu0k/">February 07, 2022 &nbsp;(1207 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sncsla/">February 08, 2022 &nbsp;(787 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/so68im/">February 09, 2022 &nbsp;(875 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/soz9c3/">February 10, 2022 &nbsp;(677 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sps0cv/">February 11, 2022 &nbsp;(751 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sqkgzp/">February 12, 2022 &nbsp;(638 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/srbmuj/">February 13, 2022 &nbsp;(534 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ss3fis/">February 14, 2022 &nbsp;(616 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ssvyex/">February 15, 2022 &nbsp;(666 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/stojvf/">February 16, 2022 &nbsp;(591 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/suhjiq/">February 17, 2022 &nbsp;(495 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/svaklf/">February 18, 2022 &nbsp;(596 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sw2z0x/">February 19, 2022 &nbsp;(475 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/swuaoz/">February 20, 2022 &nbsp;(474 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sxm6cx/">February 21, 2022 &nbsp;(703 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/syg1ff/">February 22, 2022 &nbsp;(621 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/sz9zxu/">February 23, 2022 &nbsp;(784 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t03int/">February 24, 2022 &nbsp;(918 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t0wl3r/">February 25, 2022 &nbsp;(527 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t1pqk8/">February 26, 2022 &nbsp;(362 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t2hf8a/">February 27, 2022 &nbsp;(347 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t38hj9/">February 28, 2022 &nbsp;(664 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;March 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/t40xcy/">March 01, 2022 &nbsp;(580 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t4tb6k/">March 02, 2022 &nbsp;(608 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t5kpjw/">March 03, 2022 &nbsp;(541 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t6c4mp/">March 04, 2022 &nbsp;(543 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t72xkr/">March 05, 2022 &nbsp;(332 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t7sdue/">March 06, 2022 &nbsp;(418 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t8ihdy/">March 07, 2022 &nbsp;(555 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/t9a2f4/">March 08, 2022 &nbsp;(498 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ta14l9/">March 09, 2022 &nbsp;(565 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tarzxd/">March 10, 2022 &nbsp;(644 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tbjcm9/">March 11, 2022 &nbsp;(573 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tc9ufj/">March 12, 2022 &nbsp;(353 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/td0eg1/">March 13, 2022 &nbsp;(355 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tdqip3/">March 14, 2022 &nbsp;(461 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tei6hg/">March 15, 2022 &nbsp;(641 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tfaq0y/">March 16, 2022 &nbsp;(782 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tg3c16/">March 17, 2022 &nbsp;(626 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tgul2p/">March 18, 2022 &nbsp;(715 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/thowb4/">March 19, 2022 &nbsp;(449 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tiekjh/">March 20, 2022 &nbsp;(416 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tj4u7q/">March 21, 2022 &nbsp;(559 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tjw7gq/">March 22, 2022 &nbsp;(675 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tknb4f/">March 23, 2022 &nbsp;(637 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tlz2a6/">March 24, 2022 &nbsp;(764 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tnfegt/">March 25, 2022 &nbsp;(574 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/toi6rn/">March 26, 2022 &nbsp;(445 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tpcx5o/">March 27, 2022 &nbsp;(661 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tq1pfn/">March 28, 2022 &nbsp;(796 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tqs71b/">March 29, 2022 &nbsp;(824 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/trys1g/">March 30, 2022 &nbsp;(619 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tss9p1/">March 31, 2022 &nbsp;(687 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;April 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/ttiqy2/">April 01, 2022 &nbsp;(731 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tuay9p/">April 02, 2022 &nbsp;(497 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tv1fg8/">April 03, 2022 &nbsp;(496 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tvtsa9/">April 04, 2022 &nbsp;(583 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/twn4af/">April 05, 2022 &nbsp;(640 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/txedws/">April 06, 2022 &nbsp;(570 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ty5fwy/">April 07, 2022 &nbsp;(542 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tyvuhl/">April 08, 2022 &nbsp;(753 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/tzlzhv/">April 09, 2022 &nbsp;(877 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u0aidh/">April 10, 2022 &nbsp;(829 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u0zvij/">April 11, 2022 &nbsp;(912 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u1qv5y/">April 12, 2022 &nbsp;(972 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u2ilwx/">April 13, 2022 &nbsp;(1369 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u39laj/">April 14, 2022 &nbsp;(1387 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u40f1w/">April 15, 2022 &nbsp;(1187 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u4qfal/">April 16, 2022 &nbsp;(1065 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u5fu3h/">April 17, 2022 &nbsp;(1817 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u6565a/">April 18, 2022 &nbsp;(1573 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u6x409/">April 19, 2022 &nbsp;(1956 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u7orj1/">April 20, 2022 &nbsp;(1884 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u8fr5h/">April 21, 2022 &nbsp;(1706 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u96nxl/">April 22, 2022 &nbsp;(945 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/u9xss5/">April 23, 2022 &nbsp;(647 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uan7nk/">April 24, 2022 &nbsp;(537 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ubd7y2/">April 25, 2022 &nbsp;(952 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uc4up5/">April 26, 2022 &nbsp;(1164 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ucvqli/">April 27, 2022 &nbsp;(877 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/udn9a0/">April 28, 2022 &nbsp;(834 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ueee53/">April 29, 2022 &nbsp;(955 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uf42gy/">April 30, 2022 &nbsp;(801 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;May 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/ufshns/">May 01, 2022 &nbsp;(773 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ugi0co/">May 02, 2022 &nbsp;(670 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uh8nb5/">May 03, 2022 &nbsp;(835 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uhz16g/">May 04, 2022 &nbsp;(886 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uipt94/">May 05, 2022 &nbsp;(1016 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ujfx8d/">May 06, 2022 &nbsp;(861 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uk5z3v/">May 07, 2022 &nbsp;(917 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ukuixg/">May 08, 2022 &nbsp;(841 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uljnvf/">May 09, 2022 &nbsp;(2107 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/umas2l/">May 10, 2022 &nbsp;(1335 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/un1xdr/">May 11, 2022 &nbsp;(3074 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/unt9m0/">May 12, 2022 &nbsp;(2650 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uok5qu/">May 13, 2022 &nbsp;(1502 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/up9x14/">May 14, 2022 &nbsp;(710 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/upyp5u/">May 15, 2022 &nbsp;(827 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uqo3kx/">May 16, 2022 &nbsp;(990 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/urewf8/">May 17, 2022 &nbsp;(895 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/us57z8/">May 18, 2022 &nbsp;(867 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/usvsir/">May 19, 2022 &nbsp;(967 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/utlsws/">May 20, 2022 &nbsp;(812 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uug2ve/">May 21, 2022 &nbsp;(705 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uv3xqj/">May 22, 2022 &nbsp;(585 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uvsn5y/">May 23, 2022 &nbsp;(826 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uwj41l/">May 24, 2022 &nbsp;(810 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ux9v63/">May 25, 2022 &nbsp;(791 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uxzzat/">May 26, 2022 &nbsp;(1384 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uyqk8i/">May 27, 2022 &nbsp;(1389 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/uzg6bi/">May 28, 2022 &nbsp;(715 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v042cb/">May 29, 2022 &nbsp;(549 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v0sn6p/">May 30, 2022 &nbsp;(680 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v1ikyu/">May 31, 2022 &nbsp;(1121 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;June 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/v293qs/">June 01, 2022 &nbsp;(918 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v316tn/">June 02, 2022 &nbsp;(779 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v3rtcm/">June 03, 2022 &nbsp;(753 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v4hlvj/">June 04, 2022 &nbsp;(587 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v5694r/">June 05, 2022 &nbsp;(511 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v5v535/">June 06, 2022 &nbsp;(818 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v6mzda/">June 07, 2022 &nbsp;(867 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v7hd6l/">June 08, 2022 &nbsp;(1218 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v892qr/">June 09, 2022 &nbsp;(905 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v8zybn/">June 10, 2022 &nbsp;(1168 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/v9q7q1/">June 11, 2022 &nbsp;(1550 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vaepbi/">June 12, 2022 &nbsp;(1534 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vb4d6l/">June 13, 2022 &nbsp;(2905 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vbvogd/">June 14, 2022 &nbsp;(1597 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vcmneb/">June 15, 2022 &nbsp;(1894 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vde118/">June 16, 2022 &nbsp;(1136 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ve558e/">June 17, 2022 &nbsp;(1034 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/veys2j/">June 18, 2022 &nbsp;(2112 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vfnoiz/">June 19, 2022 &nbsp;(1108 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vgdfn4/">June 20, 2022 &nbsp;(908 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vh59l6/">June 21, 2022 &nbsp;(797 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vhwzx4/">June 22, 2022 &nbsp;(769 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/viow1x/">June 23, 2022 &nbsp;(665 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vjgenp/">June 24, 2022 &nbsp;(853 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vk7cyr/">June 25, 2022 &nbsp;(572 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vkwzx1/">June 26, 2022 &nbsp;(418 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vlnig6/">June 27, 2022 &nbsp;(692 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vmexpb/">June 28, 2022 &nbsp;(588 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vn7hq5/">June 29, 2022 &nbsp;(612 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vo0190/">June 30, 2022 &nbsp;(764 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;July 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/vosi4l/">July 01, 2022 &nbsp;(599 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vpjzog/">July 02, 2022 &nbsp;(486 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vq9v0w/">July 03, 2022 &nbsp;(490 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vqzmgw/">July 04, 2022 &nbsp;(589 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vrq1kf/">July 05, 2022 &nbsp;(598 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vshw3m/">July 06, 2022 &nbsp;(620 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vtaet9/">July 07, 2022 &nbsp;(702 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vu2mgb/">July 08, 2022 &nbsp;(422 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vuu2nk/">July 09, 2022 &nbsp;(377 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vvjzyp/">July 10, 2022 &nbsp;(323 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vwabgh/">July 11, 2022 &nbsp;(605 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vx2y3z/">July 12, 2022 &nbsp;(582 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vxuyyx/">July 13, 2022 &nbsp;(584 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vynm1b/">July 14, 2022 &nbsp;(644 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/vzg7dy/">July 15, 2022 &nbsp;(656 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w08kis/">July 16, 2022 &nbsp;(773 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w0zfzy/">July 17, 2022 &nbsp;(606 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w1qwv5/">July 18, 2022 &nbsp;(1161 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w2k7yr/">July 19, 2022 &nbsp;(826 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w3docu/">July 20, 2022 &nbsp;(831 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w47twz/">July 21, 2022 &nbsp;(621 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w51ubm/">July 22, 2022 &nbsp;(646 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w5ve6t/">July 23, 2022 &nbsp;(511 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w6nm34/">July 24, 2022 &nbsp;(529 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w7fx5q/">July 25, 2022 &nbsp;(487 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w8apzr/">July 26, 2022 &nbsp;(652 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/w95mn6/">July 27, 2022 &nbsp;(697 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wa0k00/">July 28, 2022 &nbsp;(848 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wavpny/">July 29, 2022 &nbsp;(631 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wbpa6i/">July 30, 2022 &nbsp;(506 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wcgoix/">July 31, 2022 &nbsp;(627 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;August 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/wd8qph/">August 01, 2022 &nbsp;(650 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/we2rnd/">August 02, 2022 &nbsp;(756 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wexh3e/">August 03, 2022 &nbsp;(877 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wfsaw4/">August 04, 2022 &nbsp;(728 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wgmgjb/">August 05, 2022 &nbsp;(748 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/whfzp5/">August 06, 2022 &nbsp;(476 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wi7icu/">August 07, 2022 &nbsp;(543 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wj0107/">August 08, 2022 &nbsp;(918 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wjuhnb/">August 09, 2022 &nbsp;(678 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wkoo0i/">August 10, 2022 &nbsp;(1177 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wliv6s/">August 11, 2022 &nbsp;(1240 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wmciep/">August 12, 2022 &nbsp;(1147 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wn5y58/">August 13, 2022 &nbsp;(865 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wnxz9m/">August 14, 2022 &nbsp;(545 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/woqr6p/">August 15, 2022 &nbsp;(680 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wplbnk/">August 16, 2022 &nbsp;(676 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wqg1hz/">August 17, 2022 &nbsp;(609 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wrajpo/">August 18, 2022 &nbsp;(604 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ws53e5/">August 19, 2022 &nbsp;(700 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wsypnj/">August 20, 2022 &nbsp;(553 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wtr2q4/">August 21, 2022 &nbsp;(387 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wukfo1/">August 22, 2022 &nbsp;(550 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wvfqsu/">August 23, 2022 &nbsp;(719 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wwaf75/">August 24, 2022 &nbsp;(644 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wx549x/">August 25, 2022 &nbsp;(754 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wy01sl/">August 26, 2022 &nbsp;(676 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wyu2xd/">August 27, 2022 &nbsp;(516 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/wzn139/">August 28, 2022 &nbsp;(473 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x0g1yb/">August 29, 2022 &nbsp;(677 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x1a70t/">August 30, 2022 &nbsp;(798 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x24rkf/">August 31, 2022 &nbsp;(701 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;September 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/x2yrhi/">September 01, 2022 &nbsp;(765 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x3srsg/">September 02, 2022 &nbsp;(636 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x4m18u/">September 03, 2022 &nbsp;(490 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x5eg4z/">September 04, 2022 &nbsp;(442 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x67grz/">September 05, 2022 &nbsp;(754 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x71l16/">September 06, 2022 &nbsp;(1120 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x7w611/">September 07, 2022 &nbsp;(1096 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x8r22n/">September 08, 2022 &nbsp;(1016 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/x9md3j/">September 09, 2022 &nbsp;(835 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xagj2o/">September 10, 2022 &nbsp;(808 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xb9pyq/">September 11, 2022 &nbsp;(786 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xc3ttm/">September 12, 2022 &nbsp;(933 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xcyiyv/">September 13, 2022 &nbsp;(1263 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xdsyg7/">September 14, 2022 &nbsp;(4904 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xenp6l/">September 15, 2022 &nbsp;(5035 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xfi3f3/">September 16, 2022 &nbsp;(1477 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xgd5ak/">September 17, 2022 &nbsp;(920 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xh7km4/">September 18, 2022 &nbsp;(1075 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xi2eus/">September 19, 2022 &nbsp;(796 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xizkvl/">September 20, 2022 &nbsp;(843 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xjveii/">September 21, 2022 &nbsp;(1121 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xkrzap/">September 22, 2022 &nbsp;(916 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xlo0z1/">September 23, 2022 &nbsp;(870 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xmjibe/">September 24, 2022 &nbsp;(610 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xndzwc/">September 25, 2022 &nbsp;(546 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xo9nws/">September 26, 2022 &nbsp;(708 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xp720p/">September 27, 2022 &nbsp;(802 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xq3bqf/">September 28, 2022 &nbsp;(771 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xqyt74/">September 29, 2022 &nbsp;(695 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xrsqbq/">September 30, 2022 &nbsp;(497 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;October 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/xsmkzv/">October 01, 2022 &nbsp;(418 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xtfxo7/">October 02, 2022 &nbsp;(373 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xua255/">October 03, 2022 &nbsp;(592 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xv5xs8/">October 04, 2022 &nbsp;(503 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xw16ga/">October 05, 2022 &nbsp;(547 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xwwo6p/">October 06, 2022 &nbsp;(511 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xxq5dt/">October 07, 2022 &nbsp;(459 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xyjxjb/">October 08, 2022 &nbsp;(324 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/xzd0c6/">October 09, 2022 &nbsp;(308 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y05zgd/">October 10, 2022 &nbsp;(538 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y105e9/">October 11, 2022 &nbsp;(447 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y1uoig/">October 12, 2022 &nbsp;(514 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y2putc/">October 13, 2022 &nbsp;(678 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y3kkfx/">October 14, 2022 &nbsp;(469 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y4f13c/">October 15, 2022 &nbsp;(291 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y58428/">October 16, 2022 &nbsp;(297 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y61zac/">October 17, 2022 &nbsp;(426 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y6xcur/">October 18, 2022 &nbsp;(381 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y7tddk/">October 19, 2022 &nbsp;(518 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y8ovud/">October 20, 2022 &nbsp;(432 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/y9kch3/">October 21, 2022 &nbsp;(424 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yaeljx/">October 22, 2022 &nbsp;(325 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yb8m0a/">October 23, 2022 &nbsp;(337 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yc2knf/">October 24, 2022 &nbsp;(501 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ycwdpk/">October 25, 2022 &nbsp;(849 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ydpfls/">October 26, 2022 &nbsp;(829 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yej0u8/">October 27, 2022 &nbsp;(542 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yfejvu/">October 28, 2022 &nbsp;(409 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ygaiev/">October 29, 2022 &nbsp;(548 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yh61e4/">October 30, 2022 &nbsp;(308 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yi2cr7/">October 31, 2022 &nbsp;(451 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;November 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/yj0cm9/">November 01, 2022 &nbsp;(415 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yjx2bc/">November 02, 2022 &nbsp;(541 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yktt60/">November 03, 2022 &nbsp;(626 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ylqdjt/">November 04, 2022 &nbsp;(603 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ymlpvy/">November 05, 2022 &nbsp;(391 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yni80r/">November 06, 2022 &nbsp;(399 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yoec5j/">November 07, 2022 &nbsp;(519 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ypcu69/">November 08, 2022 &nbsp;(1754 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yqa8ec/">November 09, 2022 &nbsp;(1918 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yr6vee/">November 10, 2022 &nbsp;(1293 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ys2p95/">November 11, 2022 &nbsp;(1371 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ysy1o2/">November 12, 2022 &nbsp;(903 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yttcee/">November 13, 2022 &nbsp;(853 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yuqhks/">November 14, 2022 &nbsp;(994 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yvoib1/">November 15, 2022 &nbsp;(811 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ywlghu/">November 16, 2022 &nbsp;(791 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yxi8om/">November 17, 2022 &nbsp;(977 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yycn3b/">November 18, 2022 &nbsp;(608 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yz4znw/">November 19, 2022 &nbsp;(484 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/yzwmwi/">November 20, 2022 &nbsp;(588 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z0r4kc/">November 21, 2022 &nbsp;(811 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z1lypa/">November 22, 2022 &nbsp;(700 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z2h19s/">November 23, 2022 &nbsp;(638 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z3bxpv/">November 24, 2022 &nbsp;(457 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z45kuw/">November 25, 2022 &nbsp;(407 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z4zqum/">November 26, 2022 &nbsp;(339 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z5t9h8/">November 27, 2022 &nbsp;(352 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z6ohri/">November 28, 2022 &nbsp;(633 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z7l5p0/">November 29, 2022 &nbsp;(484 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/z8j5c9/">November 30, 2022 &nbsp;(616 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;December 2022</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/z9g4st/">December 01, 2022 &nbsp;(475 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zadbqz/">December 02, 2022 &nbsp;(534 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zb977b/">December 03, 2022 &nbsp;(258 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zc22xr/">December 04, 2022 &nbsp;(217 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zcymmn/">December 05, 2022 &nbsp;(398 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zdxdl6/">December 06, 2022 &nbsp;(349 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zetm2h/">December 07, 2022 &nbsp;(495 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zfqqmy/">December 08, 2022 &nbsp;(471 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zgol4x/">December 09, 2022 &nbsp;(367 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zhkjjk/">December 10, 2022 &nbsp;(299 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zihddi/">December 11, 2022 &nbsp;(234 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zjp8tx/">December 12, 2022 &nbsp;(434 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zko3pt/">December 13, 2022 &nbsp;(479 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zlj5r1/">December 14, 2022 &nbsp;(427 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zmdpjz/">December 15, 2022 &nbsp;(506 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zn7kmy/">December 16, 2022 &nbsp;(415 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/znzkda/">December 17, 2022 &nbsp;(301 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zoriq1/">December 18, 2022 &nbsp;(258 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zpjll8/">December 19, 2022 &nbsp;(310 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zqg79i/">December 20, 2022 &nbsp;(393 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zrbzbx/">December 21, 2022 &nbsp;(370 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zse1hh/">December 22, 2022 &nbsp;(398 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zt7wxy/">December 23, 2022 &nbsp;(299 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zu3882/">December 24, 2022 &nbsp;(308 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zurxt7/">December 25, 2022 &nbsp;(147 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zvgh3v/">December 26, 2022 &nbsp;(285 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zw8aor/">December 27, 2022 &nbsp;(348 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zx1yqe/">December 28, 2022 &nbsp;(310 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zxxihz/">December 29, 2022 &nbsp;(331 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zyspvz/">December 30, 2022 &nbsp;(324 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/zzn04h/">December 31, 2022 &nbsp;(332 comments)</a></li>
    </ul>
  </details>
</details>

<!-- 2021 -->
<details>
  <summary>&nbsp;2021</summary>
  <details>
    <summary>&nbsp;January 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/ko67py/">January 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kos3ok/">January 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kpf0l3/">January 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kq2mi0/">January 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kqs0np/">January 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/krhqzc/">January 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ks71wl/">January 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kswhxa/">January 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ktl91o/">January 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ku8sm9/">January 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kuwmeo/">January 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kvlswa/">January 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kwaesu/">January 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kwzq6e/">January 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kxoeid/">January 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kydbkh/">January 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kz0s7a/">January 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kzokbz/">January 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l0dmua/">January 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l0juvp/">January 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l1340q/">January 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l1sdgu/">January 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l2hg5m/">January 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l36i14/">January 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l3trrq/">January 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l4he2r/">January 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l57mq5/">January 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l5xsvi/">January 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l6pjpd/">January 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l7kyqo/">January 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l8fafk/">January 30, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/l961ub/">January 31, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;February 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/l9wbhd/">February 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/laoxw8/">February 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lbh16s/">February 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lc92jj/">February 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ld0tsy/">February 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ldr8nc/">February 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/legpl8/">February 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lf5fz3/">February 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lfw0ve/">February 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lgnaua/">February 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lheavg/">February 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/li50pk/">February 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/liulbp/">February 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ljiplj/">February 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lk75ej/">February 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lkxcln/">February 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/llnhve/">February 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lmfb92/">February 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ln8fhx/">February 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lo0oby/">February 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/loqfr4/">February 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lpgkry/">February 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lqavo6/">February 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lr591q/">February 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lrzn8b/">February 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lsralv/">February 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lthokf/">February 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lu8iq5/">February 28, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;March 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/lv1lh6/">March 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lvv97v/">March 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lwmpt0/">March 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lxdzux/">March 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ly5fug/">March 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lyvdf8/">March 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/lzkhqn/">March 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m098lz/">March 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m106rq/">March 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m1qsx4/">March 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m2j824/">March 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m3ba0d/">March 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m40dyn/">March 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m4pc9i/">March 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m5e31q/">March 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m62bc8/">March 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m6tl05/">March 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m7kdxm/">March 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m8anmd/">March 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m90wb2/">March 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/m9ptnz/">March 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/magddu/">March 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mb80at/">March 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mbysn2/">March 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mcrcgt/">March 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mdhzal/">March 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/me7xh9/">March 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/meuwl6/">March 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mfi41c/">March 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mg8cy9/">March 30, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mgykyv/">March 31, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;April 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/mho0ic/">April 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/midbun/">April 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mj1sdm/">April 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mjphqz/">April 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mkd37o/">April 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ml40yc/">April 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mluosx/">April 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mmkgdz/">April 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mna0c6/">April 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mnyfm7/">April 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mokpzr/">April 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mp773l/">April 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mpvihc/">April 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mqjl8a/">April 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mr7y7v/">April 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mrw8js/">April 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mskg4a/">April 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mt6hqa/">April 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mtthhb/">April 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/muj3af/">April 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mv8msp/">April 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mvxoow/">April 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mwns1s/">April 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mxd1e3/">April 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/my19eh/">April 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/myq125/">April 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/mzgwyp/">April 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n07d7x/">April 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n0x80l/">April 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n1mqd1/">April 30, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;May 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/n2bm4v/">May 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n2zhkj/">May 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n3ob9p/">May 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n4germ/">May 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n57t66/">May 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n5zly6/">May 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n6qs6z/">May 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n7hrcz/">May 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n86zzj/">May 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n8wdv6/">May 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/n9pa75/">May 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/naguyo/">May 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nb8vg3/">May 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nc0rpg/">May 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ncr6lf/">May 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ndgwea/">May 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ne77c3/">May 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nf1p1c/">May 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nfwjne/">May 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ngra7o/">May 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nhkhwb/">May 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nib62x/">May 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nj0gjv/">May 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/njq0tz/">May 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nkhm3u/">May 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nl8swe/">May 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nlzzgq/">May 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nmq84n/">May 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nnfz3x/">May 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/no3vom/">May 30, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/noujj7/">May 31, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;June 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/npm6aq/">June 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nqdun4/">June 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nr5cic/">June 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nrx11z/">June 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nso3sd/">June 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nte138/">June 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nu4e7f/">June 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nuwt2s/">June 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nvnp5f/">June 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nwfi05/">June 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nx7t3y/">June 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nxz0au/">June 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nyp4ur/">June 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/nzf3do/">June 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o0674j/">June 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o0x4xk/">June 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o1ozff/">June 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o2h3v2/">June 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o38mp4/">June 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o3y0op/">June 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o4nihc/">June 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o5eut2/">June 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o65z2m/">June 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o6tzw3/">June 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o7gucu/">June 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o847wy/">June 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o8qh8y/">June 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/o9dd0z/">June 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oa1foh/">June 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oaq1qj/">June 30, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;July 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/obendw/">July 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oc37iy/">July 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ocrexn/">July 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oddn3f/">July 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oe0668/">July 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oeo547/">July 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ofc5u5/">July 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/og0dce/">July 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ogokg5/">July 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ohcd31/">July 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ohy7il/">July 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oikg71/">July 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oj8n3l/">July 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ojx9si/">July 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oklty4/">July 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ol9zl6/">July 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/olxt21/">July 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/omk1cf/">July 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/on795c/">July 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/onvbnr/">July 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ooj7qo/">July 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/op73ks/">July 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/opvbuz/">July 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oqjevp/">July 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/or5del/">July 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/orruz4/">July 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/osgce0/">July 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ot376j/">July 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/otqvqc/">July 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oue5av/">July 30, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ov15s3/">July 31, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;August 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/ovm2lr/">August 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ow7ugi/">August 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/owwcna/">August 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oxlf7j/">August 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oyakfh/">August 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/oyzyjs/">August 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ozn2mj/">August 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p08jl0/">August 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p0upcl/">August 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p1ihxy/">August 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p26ba1/">August 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p2t1uj/">August 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p3grli/">August 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p41sp2/">August 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p4nb3l/">August 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p59e1r/">August 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p5x5yd/">August 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p6kicu/">August 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p78a2k/">August 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p7vh1x/">August 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p8lffr/">August 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p96fvo/">August 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/p9swaz/">August 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pagoum/">August 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pb4dyc/">August 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pbsnnw/">August 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pcgkwh/">August 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pd3n6h/">August 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pdp4ch/">August 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pebdg0/">August 30, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pez5xw/">August 31, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;September 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/pfmz68/">September 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pgb42p/">September 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pgygf1/">September 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/phl9hm/">September 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pi6thn/">September 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pisps0/">September 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pjgb5j/">September 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pk3y0n/">September 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pkr4fx/">September 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pleg2a/">September 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pm12mh/">September 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pmmgyu/">September 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pn8tku/">September 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pnw9dd/">September 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pojhe2/">September 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pp6t1h/">September 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pptqfr/">September 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pqg62q/">September 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pr1oeq/">September 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pro1m2/">September 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/psbw5t/">September 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pt0de0/">September 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pto076/">September 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/puct3u/">September 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pv02vf/">September 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pvn7wa/">September 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pwa5wh/">September 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pwz2p9/">September 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pxobts/">September 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pycu5v/">September 30, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;October 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/pz0zxg/">October 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/pzorc4/">October 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q0b3jx/">October 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q0yqwk/">October 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q1nu64/">October 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q2di7p/">October 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q31rj5/">October 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q3qswp/">October 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q4ek2w/">October 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q51hvk/">October 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q5om1m/">October 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q6elem/">October 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q73zel/">October 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q7stvx/">October 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q8h5hn/">October 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q95ahi/">October 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/q9s502/">October 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qafrz4/">October 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qb4dpm/">October 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qbtchn/">October 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qck1hn/">October 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qd9po7/">October 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qdy860/">October 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qelcgj/">October 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qf9fnc/">October 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qfz2k0/">October 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qgoyxi/">October 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qhfeln/">October 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qi558c/">October 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qiudz1/">October 30, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qjjbjn/">October 31, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;November 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/qk7ooa/">November 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qkxqge/">November 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qlo2v9/">November 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qme5j5/">November 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qn4lsp/">November 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qnu34x/">November 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qoifvo/">November 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qp7by8/">November 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qpx82f/">November 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qqnkng/">November 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qref4w/">November 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qs4t9e/">November 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qsuruc/">November 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qtjebc/">November 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qu9jyy/">November 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qv0zrj/">November 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qvsj0t/">November 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qwj675/">November 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qx9p39/">November 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qxz754/">November 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qyoign/">November 21, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/qzejcz/">November 22, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r06f3u/">November 23, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r0xzvr/">November 24, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r1pjz2/">November 25, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r2gavz/">November 26, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r36uqg/">November 27, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r3xc6y/">November 28, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r4p0bf/">November 29, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r5gd2a/">November 30, 2021 &nbsp;( comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;December 2021</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/r67vkm/">December 01, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r70ghj/">December 02, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r7s2wl/">December 03, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r8j147/">December 04, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/r991sy/">December 05, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ra05m4/">December 06, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ras7o3/">December 07, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rbk9tl/">December 08, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rcb6qu/">December 09, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rd1tmi/">December 10, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rdt3xc/">December 11, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/reii8n/">December 12, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rf8qle/">December 13, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rg0r79/">December 14, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rgs3x3/">December 15, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rhk4jy/">December 16, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rialjg/">December 17, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rj0vqu/">December 18, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rjqbgk/">December 19, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rkg6bg/">December 20, 2021 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rl7rdl/">December 21, 2021 &nbsp;(937 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rlyik8/">December 22, 2021 &nbsp;(795 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rmoqo3/">December 23, 2021 &nbsp;(888 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rnfl39/">December 24, 2021 &nbsp;(698 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ro3qp7/">December 25, 2021 &nbsp;(616 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/roqpq2/">December 26, 2021 &nbsp;(535 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rpgcip/">December 27, 2021 &nbsp;(761 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rq8gc2/">December 28, 2021 &nbsp;(797 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rr0uhq/">December 29, 2021 &nbsp;(982 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rru7pv/">December 30, 2021 &nbsp;(673 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/rsmzgz/">December 31, 2021 &nbsp;(861 comments)</a></li>
    </ul>
  </details>
</details>

<!-- 2020 -->
<details>
  <summary>&nbsp;2020</summary>
  <details>
    <summary>&nbsp;November 2020</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/jo9yfx/">November 05, 2020 &nbsp;(109 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;December 2020</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/kcrx35/">December 14, 2020 &nbsp;(645 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kdg31g/">December 15, 2020 &nbsp;(622 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/ke3ljf/">December 16, 2020 &nbsp;(1585 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kerp5j/">December 17, 2020 &nbsp;(1384 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kffgjf/">December 18, 2020 &nbsp;(710 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kgotp3/">December 20, 2020 &nbsp;(772 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/khbe7f/">December 21, 2020 &nbsp;(745 comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/khzfmm/">December 22, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kinhju/">December 23, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kja0bs/">December 24, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kju63a/">December 25, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kkdprg/">December 26, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kkyghm/">December 27, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/klkl5o/">December 28, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/km8gzh/">December 29, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/kmwen5/">December 30, 2020 &nbsp;( comments)</a></li>
      <li><a href="https://reddit.com/r/ethfinance/comments/knka89/">December 31, 2020 &nbsp;( comments)</a></li>
    </ul>
  </details>
</details>

<!-- 2019 -->
<details>
  <summary>&nbsp;2019</summary>
  <details>
    <summary>&nbsp;September 2019</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/d1991u/">September 08, 2019 &nbsp;(223 comments)</a></li>
    </ul>
  </details>
  <details>
    <summary>&nbsp;December 2019</summary>
    <ul>
      <li><a href="https://reddit.com/r/ethfinance/comments/eagfun/">December 14, 2019 &nbsp;(307 comments)</a></li>
    </ul>
  </details>
</details>


