---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<div class="visitor-map-container">
  <div class="visitor-map-header">
    <h1><i class="fas fa-globe-americas"></i> Visitor Map</h1>
    <p class="subtitle">See where your visitors are coming from around the world</p>
  </div>

  <div class="map-stats-container">
    <div class="map-wrapper">
      <div id="map" class="visitor-map"></div>
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
  }

  .visitor-map {
    height: 600px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border: 1px solid #e0e0e0;
  }

  .stats-panel {
    flex: 1;
    min-width: 250px;
    background: #f9f9f9;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }

  .stats-panel h2 {
    color: #2c3e50;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
    margin-top: 0;
  }

  .stat-card {
    display: flex;
    align-items: center;
    background: white;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s;
  }

  .stat-card:hover {
    transform: translateY(-2px);
  }

  .stat-icon {
    font-size: 24px;
    color: #3498db;
    margin-right: 15px;
    width: 40px;
    text-align: center;
  }

  .stat-label {
    font-size: 0.9em;
    color: #7f8c8d;
  }

  .stat-value {
    font-size: 1.5em;
    font-weight: bold;
    color: #2c3e50;
  }

  @media (max-width: 768px) {
    .map-stats-container {
      flex-direction: column;
    }
  }
</style>

<script>
  function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 2,
      center: { lat: 20, lng: 0 },
      styles: [
        {
          "featureType": "administrative",
          "elementType": "labels.text.fill",
          "stylers": [{"color": "#444444"}]
        },
        {
          "featureType": "landscape",
          "elementType": "all",
          "stylers": [{"color": "#f2f2f2"}]
        },
        {
          "featureType": "poi",
          "elementType": "all",
          "stylers": [{"visibility": "off"}]
        },
        {
          "featureType": "road",
          "elementType": "all",
          "stylers": [{"saturation": -100}, {"lightness": 45}]
        },
        {
          "featureType": "road.highway",
          "elementType": "all",
          "stylers": [{"visibility": "simplified"}]
        },
        {
          "featureType": "road.arterial",
          "elementType": "labels.icon",
          "stylers": [{"visibility": "off"}]
        },
        {
          "featureType": "transit",
          "elementType": "all",
          "stylers": [{"visibility": "off"}]
        },
        {
          "featureType": "water",
          "elementType": "all",
          "stylers": [{"color": "#d4e6f4"}, {"visibility": "on"}]
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

      // Calculate marker size based on visit count
      const markerSize = Math.min(Math.max(item.count, 5), 15);
      
      const marker = new google.maps.Marker({
        position: { lat, lng: lon },
        map,
        title: `${item.city}, ${item.country}`,
        icon: {
          path: google.maps.SymbolPath.CIRCLE,
          scale: markerSize,
          fillColor: "#e74c3c",
          fillOpacity: 0.8,
          strokeColor: "#c0392b",
          strokeWeight: 1
        }
      });

      const infoWindow = new google.maps.InfoWindow({
        content: `
          <div class="map-info-window">
            <h3>${item.city}, ${item.country}</h3>
            <p><i class="fas fa-users"></i> <strong>${item.count}</strong> visit${item.count > 1 ? 's' : ''}</p>
          </div>
        `
      });

      marker.addListener("click", () => {
        infoWindow.open(map, marker);
      });
    }
  }
</script>

<!-- Load Font Awesome for icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<!-- Replace YOUR_API_KEY below with your actual API key -->
<script async
  src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAT67_M0K-_BKk8hXRfFIA1ewg6_2WxlCU&callback=initMap">
</script>
