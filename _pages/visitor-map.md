---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<div class="visitor-map-container">
  <header class="map-header">
    <h1><i class="fas fa-globe-americas"></i> Visitor Map</h1>
    <p class="subtitle">See where our visitors are coming from around the world</p>
  </header>

  <div class="map-card">
    <div id="map" class="map-embed"></div>
  </div>

  <div class="stats-card">
    <h2><i class="fas fa-chart-line"></i> Statistics</h2>
    <div class="stats-grid">
      <div class="stat-item">
        <div class="stat-value">{{ site.data.visitors | size }}</div>
        <div class="stat-label">Total Visits</div>
      </div>
      <div class="stat-item">
        <div class="stat-value">{{ site.data.visitors | group_by: "ip" | size }}</div>
        <div class="stat-label">Unique Visitors</div>
      </div>
    </div>
  </div>
</div>

<script>
  function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 2,
      center: { lat: 20, lng: 0 },
      styles: [
        {
          "featureType": "administrative",
          "elementType": "geometry",
          "stylers": [{ "visibility": "off" }]
        },
        {
          "featureType": "poi",
          "stylers": [{ "visibility": "off" }]
        },
        {
          "featureType": "road",
          "elementType": "labels.icon",
          "stylers": [{ "visibility": "off" }]
        },
        {
          "featureType": "transit",
          "stylers": [{ "visibility": "off" }]
        }
      ]
    });

    const data = {{ site.data.visitors | jsonify }};
    const grouped = {};

    data.forEach(entry => {
      if (!entry.loc || !entry.city || !entry.country) return;
      const key = `${entry.city}|${entry.country}|${entry.loc}`;
      if (!grouped[key]) {
        grouped[key] = { count: 0, loc: entry.loc, city: entry.city, country: entry.country };
      }
      grouped[key].count += 1;
    });

    for (const key in grouped) {
      const item = grouped[key];
      const [lat, lon] = item.loc.split(',').map(Number);
      if (isNaN(lat) || isNaN(lon)) continue;

      const marker = new google.maps.Marker({
        position: { lat, lng: lon },
        map,
        title: `${item.city}, ${item.country}`,
        icon: {
          url: "https://maps.google.com/mapfiles/ms/icons/red-dot.png"
        }
      });

      const infoWindow = new google.maps.InfoWindow({
        content: `
          <div class="info-window">
            <h3>${item.city}, ${item.country}</h3>
            <p><i class="fas fa-users"></i> Visits: ${item.count}</p>
          </div>
        `
      });

      marker.addListener("click", () => {
        infoWindow.open(map, marker);
      });
    }
  }
</script>

<script async
  src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAT67_M0K-_BKk8hXRfFIA1ewg6_2WxlCU&callback=initMap">
</script>

<style>
.visitor-map-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Segoe UI', 'Roboto', sans-serif;
  color: #333;
}

.map-header {
  text-align: center;
  margin-bottom: 2rem;
}

.map-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.map-header .subtitle {
  font-size: 1.1rem;
  color: #7f8c8d;
  margin: 0;
}

.map-card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  overflow: hidden;
}

.map-embed {
  height: 500px;
  width: 100%;
}

.stats-card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
}

.stats-card h2 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  color: #2c3e50;
  font-size: 1.5rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.stat-item {
  text-align: center;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #3498db;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.9rem;
  color: #7f8c8d;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.info-window {
  padding: 0.5rem;
  font-family: 'Segoe UI', sans-serif;
}

.info-window h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
}

.info-window p {
  margin: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.fas, .fab {
  margin-right: 0.5rem;
  color: #3498db;
}

@media (max-width: 768px) {
  .visitor-map-container {
    padding: 1rem;
  }
  
  .map-header h1 {
    font-size: 2rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>
