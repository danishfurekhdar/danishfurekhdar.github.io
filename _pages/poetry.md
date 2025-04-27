---
layout: archive
title: "Poetry"
permalink: /poetry/
---
<div class="poetry-header">
  <h1>Whispers of the Soul</h1>
  <p class="subtitle">A Collection of Verse</p>
</div>

<div class="poetry-container">
  {% for poem in site.data.poetry %}
    <div class="poem-card">
      <h2 class="poem-title">{{ poem.title }}</h2>
      <div class="poem-content">
        {{ poem.content | markdownify }}
      </div>
      {% if poem.date %}
        <p class="poem-date">{{ poem.date | date: "%B %Y" }}</p>
      {% endif %}
    </div>
  {% endfor %}
</div>

<style>
  .poetry-header {
    text-align: center;
    margin: 4rem 0 3rem;
    padding: 2rem 0;
    border-bottom: 1px solid #f0f0f0;
  }

  .poetry-header h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 400;
    margin-bottom: 0.5rem;
    color: #333;
  }

  .subtitle {
    font-family: 'Crimson Text', serif;
    font-style: italic;
    font-size: 1.5rem;
    color: #888;
    margin-top: 0;
  }

  .poetry-container {
    max-width: 700px;
    margin: 0 auto;
    padding: 0 1rem;
  }

  .poem-card {
    margin: 4rem auto;
    padding: 2rem;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    border-radius: 3px;
    transition: transform 0.3s ease;
  }

  .poem-card:hover {
    transform: translateY(-3px);
  }

  .poem-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 400;
    color: #222;
    margin-bottom: 2rem;
    text-align: center;
  }

  .poem-content {
    font-family: 'Crimson Text', serif;
    font-size: 1.25rem;
    line-height: 1.8;
    color: #444;
    white-space: pre-wrap;
    text-align: center;
  }

  .poem-content p {
    margin: 1.5rem 0;
  }

  .poem-date {
    font-family: 'Crimson Text', serif;
    font-size: 1rem;
    color: #999;
    text-align: center;
    margin-top: 2rem;
    font-style: italic;
  }

  @media (max-width: 768px) {
    .poetry-header h1 {
      font-size: 2.5rem;
    }
    
    .poem-card {
      padding: 1.5rem;
      margin: 3rem auto;
    }
    
    .poem-title {
      font-size: 1.75rem;
    }
    
    .poem-content {
      font-size: 1.1rem;
    }
  }
</style>
