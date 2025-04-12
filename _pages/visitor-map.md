---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<h2>Visitor Map</h2>
<div id="map" style="height: 500px;"></div>

<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<script>
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Load from your GitHub repo raw file
fetch("https://raw.githubusercontent.com/danishfurekhdar/danishfurekhdar.github.io/main/_data/visitors.json")
  .then(res => res.json())
  .then(data => {
    data.forEach(v => {
      if (v.loc) {
        const [lat, lon] = v.loc.split(",");
        L.marker([parseFloat(lat), parseFloat(lon)])
          .addTo(map)
          .bindPopup(`Visitor from ${v.city}, ${v.country}`);
      }
    });
  });
</script>
