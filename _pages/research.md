---
layout: default
title: "Research"
permalink: /research/
---

## 📊 Google Scholar Metrics

**Name:** {{ site.data.scholar.name }}  
**Affiliation:** {{ site.data.scholar.affiliation }}

- **h-index:** {{ site.data.scholar.h_index }}
- **i10-index:** {{ site.data.scholar.i10_index }}
- **Total Citations:** {{ site.data.scholar.citations }}

[🔗 View Google Scholar Profile]({{ site.data.scholar.url }})

---

## 📄 Top 5 Publications

{% for pub in site.data.scholar_publications %}
- **{{ pub.title }}**, *{{ pub.venue }}* ({{ pub.year }})  
  Citations: {{ pub.citations }}{% if pub.url %} — [View]({{ pub.url }}){% endif %}
{% endfor %}

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
        data: [4, 22, 34, 45, 19], // Replace with real data when available
        borderWidth: 1,
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        borderColor: 'rgba(54, 162, 235, 1)'
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
</script>
