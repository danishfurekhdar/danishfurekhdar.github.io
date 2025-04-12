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
  <p>Total visits: <strong>{{ site.data.visitors | size }}</strong></p>
  <p>Unique visitors: <strong>{{ site.data.visitors | group_by: "ip" | size }}</strong></p>
</div>

<script>
  var map = L.map('map').setView([20, 0], 2);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 6,
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  // Group by city+loc for aggregated counts
  const rawData = {{ site.data.visitors | jsonify }};
  const grouped = {};

  rawData.forEach(entry => {
    const key = entry.city + '|' + entry.loc + '|' + entry.country;
    if (!grouped[key]) {
      grouped[key] = { count: 0, loc: entry.loc, city: entry.city, country: entry.country };
    }
    grouped[key].count += 1;
  });

  for (const key in grouped) {
    const group = grouped[key];
    const [lat, lon] = group.loc.split(',').map(parseFloat);
    if (!isNaN(lat) && !isNaN(lon)) {
      L.marker([lat, lon]).addTo(map)
        .bindPopup(`${group.city}, ${group.country}<br>Visits: ${group.count}`);
    }
  }
</script>
