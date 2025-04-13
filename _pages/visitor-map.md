---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<div class="visitor-map-container">
  <div class="map-stats-container">
    <div class="map-wrapper">
      <div id="map"></div>
    </div>

    <div class="stats-panel">
      <h2><i class="fas fa-chart-bar"></i> Statistics</h2>
      <div class="stat-card">
        <div class="stat-icon"><i class="fas fa-users"></i></div>
        <div class="stat-content">
          <div class="stat-label">Total Visits</div>
          <div class="stat-value">{{ site.data.visitors | size }}</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon"><i class="fas fa-user-friends"></i></div>
        <div class="stat-content">
          <div class="stat-label">Unique Visitors</div>
          <div class="stat-value">{{ site.data.visitors | group_by: "ip" | size }}</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon"><i class="fas fa-map-marked-alt"></i></div>
        <div class="stat-content">
          <div class="stat-label">Locations</div>
          <div class="stat-value">{{ site.data.visitors | group_by: "loc" | size }}</div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .visitor-map-container {
    font-family: 'Segoe UI', 'Roboto', sans-serif;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    color: #333;
  }

  .visitor-map-header {
    text-align: center;
    margin-bottom: 30px;
  }

  .visitor-map-header h1 {
    color: #2c3e50;
    margin-bottom: 5px;
  }

  .subtitle {
    color: #7f8c8d;
    font-size: 1.1em;
    margin-top: 0;
  }

  .map-stats-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }

  .map-wrapper {
    flex: 2;
    min-width: 300px;
    position: relative;
  }

  .visitor-map {
    height: 600px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border: 1px solid #e0e0e0;
  }

  .map-error-message {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: #f8d7da;
    color: #721c24;
    border-radius: 12px;
    display: none;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    padding: 20px;
  }

  .map-error-message i {
    font-size: 3em;
    margin-bottom: 15px;
    color: #dc3545;
  }

  .stats-panel {
    flex: 1;
    min-width: 250px;
    background: #f9f9f9;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }

  .stat-card {
    display: flex;
    gap: 15px;
    margin-bottom: 20px;
  }

  .stat-icon i {
    font-size: 24px;
    color: #3498db;
  }

  .stat-content .stat-label {
    font-size: 0.9em;
    color: #888;
  }

  .stat-content .stat-value {
    font-size: 1.3em;
    font-weight: bold;
  }
</style>

<script>
  function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 2,
      center: { lat: 20, lng: 0 },
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
      });

      const infoWindow = new google.maps.InfoWindow({
        content: `<strong>${item.city}, ${item.country}</strong><br>Visits: ${item.count}`
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
<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
