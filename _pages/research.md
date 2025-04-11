---
layout: page
title: "Research"
permalink: /research/
---

## 📊 Scopus Metrics

**Name:** {{ site.data.scopus.name }}  
**Affiliation:** {{ site.data.scopus.affiliation }}

- **h-index:** {{ site.data.scopus.h_index }}
- **Total Citations:** {{ site.data.scopus.citation_count }}
- **Publications:** {{ site.data.scopus.document_count }}

[🔗 View Scopus Profile]({{ site.data.scopus.profile_url }})

---

## 📄 Top 5 Publications

{% for pub in site.data.publications %}
- **{{ pub.title }}**, *{{ pub.journal }}* ({{ pub.year }})  
  Citations: {{ pub.citations }}{% if pub.doi %} — [DOI](https://doi.org/{{ pub.doi }}){% endif %}
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
        data: [4, 22, 34, 45, 19],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
</script>
