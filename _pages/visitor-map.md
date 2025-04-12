---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<h2>Visitor Map</h2>
<div id="map" style="height: 500px;"></div>

<!-- Leaflet -->
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<script>
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Load visitor data from your Sheet (published as JSON)
fetch('https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/gviz/tq?tqx=out:json')
  .then(res => res.text())
  .then(text => {
    const json = JSON.parse(text.substr(47).slice(0, -2));
    const rows = json.table.rows;

    rows.forEach(row => {
      const loc = row.c[2].v.split(","); // Assuming loc = "lat,lng"
      const country = row.c[3].v;
      L.marker([parseFloat(loc[0]), parseFloat(loc[1])])
        .addTo(map)
        .bindPopup(`Visitor from ${country}`);
    });
  });
</script>
