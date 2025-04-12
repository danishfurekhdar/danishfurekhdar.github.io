---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<h2>Visitor Map</h2>

<!-- 🗺️ Map Container -->
<div id="map" style="height: 500px; width: 100%; margin-top: 20px; border: 1px solid #ccc;"></div>

<!-- 🧩 Leaflet CSS & JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<script>
  // ✅ Initialize the map
  const map = L.map('map').setView([20, 0], 2); // Global view

  // ✅ Add OpenStreetMap tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors',
    maxZoom: 18
  }).addTo(map);

  // ✅ Fetch visitors.json from GitHub
  fetch("https://raw.githubusercontent.com/danishfurekhdar/danishfurekhdar.github.io/main/_data/visitors.json")
    .then(response => response.json())
    .then(data => {
      if (!Array.isArray(data)) {
        console.error("JSON is not an array:", data);
        return;
      }

      let count = 0;

      data.forEach(visitor => {
        if (visitor.loc) {
          const [lat, lon] = visitor.loc.split(",").map(Number);

          if (!isNaN(lat) && !isNaN(lon)) {
            L.marker([lat, lon])
              .addTo(map)
              .bindPopup(`Visitor from ${visitor.city}, ${visitor.country}<br><small>${visitor.timestamp}</small>`);
            count++;
          }
        }
      });

      console.log(`✅ ${count} visitors plotted on the map.`);
    })
    .catch(err => {
      console.error("❌ Failed to load visitor data:", err);
    });
</script>
