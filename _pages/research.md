---
layout: archive
title: "Research"
permalink: /research/
---

<!-- Inline styling for now; move to CSS file if needed -->
<style>
  .card {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
  }

  .card h2 {
    margin-top: 0;
    font-size: 1.6rem;
    color: #004d99;
  }

  .card ul {
    padding-left: 1.2rem;
  }

  .metric-item {
    margin-bottom: 0.3rem;
  }

  .pub-item {
    margin-bottom: 1.2rem;
  }

  .pub-title {
    font-weight: 600;
    font-size: 1.05rem;
  }

  .pub-meta {
    font-size: 0.9rem;
    color: #555;
  }

  .link {
    font-weight: 600;
    color: #0066cc;
  }

  canvas {
    display: block;
    margin: 0 auto;
  }
</style>

<div class="card">
  <h2>📊 Google Scholar Metrics</h2>
  <p class="metric-item"><strong>Name:</strong> {{ site.data.scholar.name }}</p>
  <p class="metric-item"><strong>Affiliation:</strong> {{ site.data.scholar.affiliation }}</p>
  <ul>
    <li><strong>h-index:</strong> {{ site.data.scholar.h_index }}</li>
    <li><strong>i10-index:</strong> {{ site.data.scholar.i10_index }}</li>
    <li><strong>Total Citations:</strong> {{ site.data.scholar.citations }}</li>
  </ul>
  <p><a class="link" href="{{ site.data.scholar.url }}" target="_blank">🔗 View Google Scholar Profile</a></p>
</div>

<div class="card">
  <h2>📄 Top 5 Publications</h2>
  {% for pub in site.data.scholar_publications %}
    <div class="pub-item">
      <div class="pub-title">{{ pub.title }}</div>
      <div class="pub-meta">
        {{ pub.venue }} ({{ pub.year }})  
        <br>
        Citations: {{ pub.citations }}{% if pub.url %} — <a href="{{ pub.url }}" class="link" target="_blank">View</a>{% endif %}
      </div>
    </div>
  {% endfor %}
</div>

<div class="card">  <!-- Changed from citation-card to card for consistency -->
  <h2>📈 Citation Trend</h2>
  <canvas id="citationChart"></canvas> <!-- Removed fixed width/height -->
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1"></script> <!-- Pinned version -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Debug: Check if data is loading
    console.log("Citation data:", {
      {% for item in site.data.scholar_citations %}
        "{{ item[0] }}": {{ item[1] }}{% unless forloop.last %},{% endunless %}
      {% endfor %}
    });

    const ctx = document.getElementById('citationChart').getContext('2d');
    
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          {% for item in site.data.scholar_citations %}
            "{{ item[0] }}"{% unless forloop.last %},{% endunless %}
          {% endfor %}
        ],
        datasets: [{
          label: 'Citations per Year',
          data: [
            {% for item in site.data.scholar_citations %}
              {{ item[1] }}{% unless forloop.last %},{% endunless %}
            {% endfor %}
          ],
          backgroundColor: 'rgba(0, 123, 255, 0.6)',
          borderColor: 'rgba(0, 123, 255, 1)',
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'top',
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Number of Citations'
            },
            ticks: {
              stepSize: 1
            }
          },
          x: {
            title: {
              display: true,
              text: 'Year'
            }
          }
        }
      }
    });
  });
</script>
