---
layout: archive
title: "Research"
permalink: /research/
---

<style>
  .metrics-card {
    border: 1px solid #e1e4e8;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 2rem;
    background-color: #f9f9f9;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  }
  .metrics-card h2 {
    margin-top: 0;
  }
  .pub-list li {
    margin-bottom: 1.2rem;
  }
  .pub-title {
    font-weight: bold;
  }
  .pub-meta {
    font-size: 0.9em;
    color: #555;
  }
</style>

<div class="metrics-card">
  <h2>📊 Google Scholar Metrics</h2>
  <p><strong>Name:</strong> {{ site.data.scholar.name }}</p>
  <p><strong>Affiliation:</strong> {{ site.data.scholar.affiliation }}</p>
  <ul>
    <li><strong>h-index:</strong> {{ site.data.scholar.h_index }}</li>
    <li><strong>i10-index:</strong> {{ site.data.scholar.i10_index }}</li>
    <li><strong>Total Citations:</strong> {{ site.data.scholar.citations }}</li>
  </ul>
  <p>
    <a href="{{ site.data.scholar.url }}" target="_blank" style="font-weight: bold;">
      🔗 View Google Scholar Profile
    </a>
  </p>
</div>

---

## 📝 Top Publications

<ul class="pub-list">
  {% for pub in site.data.scholar_publications %}
  <li>
    <div class="pub-title">{{ pub.title }}</div>
    <div class="pub-meta">
      {{ pub.venue }} ({{ pub.year }})<br>
      Citations: {{ pub.citations }}
      {% if pub.url %}
        — <a href="{{ pub.url }}" target="_blank">View</a>
      {% endif %}
    </div>
  </li>
  {% endfor %}
</ul>

---

## 📈 Citation Trend (Placeholder)

<canvas id="citChart" width="600" height="300"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const ctx = document.getElementById('citChart');
  const chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['2020', '2021', '2022', '2023', '2024'],
      datasets: [{
        label: 'Citations per Year',
        data: [4, 22, 34, 45, 19],  // Replace with real values if available
        backgroundColor: 'rgba(0, 123, 255, 0.6)',
        borderColor: 'rgba(0, 123, 255, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Citations'
          }
        }
      }
    }
  });
</script>
