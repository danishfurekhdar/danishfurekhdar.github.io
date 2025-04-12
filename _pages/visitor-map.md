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
const map = L.map('map').setView([20, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Load your visitors.json from GitHub
fetch("https://raw.githubusercontent.com/danishfurekhdar/danishfurekhdar.github.io/main/_data/visitors.json")
  .then(res => res.json())
  .then(data => {
    data.forEach(visitor => {
      if (visitor.loc) {
        const [lat, lng] = visitor.loc.split(",");
        L.marker([parseFloat(lat), parseFloat(lng)])
          .addTo(map)
          .bindPopup(`Visitor from ${visitor.city}, ${visitor.country}`);
      }
    });
  })
  .catch(err => {
    console.error("Error loading visitor data:", err);
  });
</script>
