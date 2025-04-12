---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<div style="font-family: 'Segoe UI', sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px;">
  <h1>🌍 Visitor Map</h1>
  <div id="map" style="height: 500px; border-radius: 8px; margin-bottom: 30px;"></div>

  <h2>📈 Statistics</h2>
  <p>Total visits: <strong>{{ site.data.visitors.size }}</strong></p>
  <p>Unique visitors: <strong>{{ site.data.visitors | group_by: "ip" | size }}</strong></p>
</div>

<script>
  var map = L.map('map').setView([20, 0], 2);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 6,
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  {% assign grouped = site.data.visitors | group_by_exp: "item", "item.city | append: ',' | append: item.country" %}
  {% for group in grouped %}
    {% assign visitor = group.items[0] %}
    {% if visitor.lat and visitor.lon %}
      L.marker([{{ visitor.lat }}, {{ visitor.lon }}]).addTo(map)
        .bindPopup("{{ visitor.city }}, {{ visitor.country }}<br>Visits: {{ group.size }}");
    {% endif %}
  {% endfor %}
</script>
