---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<h2>Visitor Map</h2>
<div id="map" style="height: 500px;"></div>

<!-- Leaflet CSS and JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<script>
const map = L.map('map').setView([20, 0], 2); // World view

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

fetch("https://raw.githubusercontent.com/danishfurekhdar/danishfurekhdar.github.io/main/_data/visitors.json")
  .then(res => res.json())
  .then(data => {
    if (!Array.isArray(data)) {
      console.error("Expected array, got:", data);
      return;
    }

    let count = 0;

    data.forEach(visitor => {
      if (visitor.loc && visitor.city && visitor.country) {
        const [lat, lon] = visitor.loc.split(',').map(Number);

        if (!isNaN(lat) && !isNaN(lon)) {
          L.marker([lat, lon])
            .addTo(map)
            .bindPopup(`Visitor from ${visitor.city}, ${visitor.country}<br><small>${visitor.timestamp}</small>`);

          count++;
        }
      }
    });

    console.log(`✅ Plotted ${count} visitors.`);
  })
  .catch(err => {
    console.error("❌ Failed to load visitor data:", err);
  });
</script>
