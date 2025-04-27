---
layout: page
title: "Poetry"
permalink: /poetry/
---
<div style="text-align: center; margin-top: 2rem;">
  <h1 style="font-family: 'Georgia', serif; font-size: 3rem;">Poetry Collection</h1>
  <p style="font-style: italic; color: gray;">Echoes from the Heart</p>
</div>

{% for poem in site.data.poetry %}
  <div style="margin: 3rem auto; max-width: 700px; text-align: center; font-family: 'Georgia', serif;">
    <h2 style="font-size: 2rem;">{{ poem.title }}</h2>
    <p style="white-space: pre-wrap; font-size: 1.2rem; line-height: 2; margin-top: 1rem;">{{ poem.content }}</p>
  </div>
{% endfor %}
