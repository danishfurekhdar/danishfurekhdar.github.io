---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<h2>Visitor Map</h2>

<!-- 🗺️ Map Container -->
<div id="map" style="height: 500px; width: 100%; margin-top: 20px; border: 1px solid #ccc;"></div>

<!-- 🧩 Leaflet CSS & JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" 
    integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
    crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
    integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
    crossorigin=""></script>

<script>
  // Wait for DOM to be fully loaded
  document.addEventListener('DOMContentLoaded', function() {
    // ✅ Initialize the map
    const map = L.map('map').setView([20, 0], 2); // Global view

    // ✅ Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 18
    }).addTo(map);

    // Add a fallback in case the container isn't properly sized
    setTimeout(() => {
      map.invalidateSize();
    }, 100);

    // ✅ Fetch visitors.json from GitHub
    fetch("https://raw.githubusercontent.com/danishfurekhdar/danishfurekhdar.github.io/main/_data/visitors.json")
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
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
                .bindPopup(`Visitor from ${visitor.city || 'unknown city'}, ${visitor.country || 'unknown country'}<br><small>${visitor.timestamp || 'unknown time'}</small>`);
              count++;
            }
          }
        });

        console.log(`✅ ${count} visitors plotted on the map.`);
      })
      .catch(err => {
        console.error("❌ Failed to load visitor data:", err);
        // Add a fallback marker to show the map is working
        L.marker([20, 0]).addTo(map)
          .bindPopup("Couldn't load visitor data. See console for details.");
      });
  });
</script>
