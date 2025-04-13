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
      <div id="map-error" class="map-error-message" style="display:none;">
        <i class="fas fa-exclamation-triangle"></i>
        <p>Map failed to load. Please check your internet connection or API key.</p>
      </div>
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
  const MAPS_API_KEY = 'AIzaSyAT67_M0K-_BKk8hXRfFIA1ewg6_2WxlCU'; // Replace this manually or via GitHub Actions

  function initMap() {
    const mapElement = document.getElementById('map');
    if (!mapElement) return showMapError();

    const map = new google.maps.Map(mapElement, {
      center: { lat: 20, lng: 0 },
      zoom: 2,
      styles: [
        { featureType: "water", elementType: "geometry", stylers: [{ color: "#d4e6f4" }] },
        { featureType: "landscape", elementType: "geometry", stylers: [{ color: "#f5f5f5" }] }
      ]
    });

    const visitors = {{ site.data.visitors | jsonify }};
    const locations = {};

    visitors.forEach(entry => {
      if (!entry.loc || !entry.city || !entry.country) return;
      const [lat, lon] = entry.loc.split(',').map(Number);
      if (isNaN(lat) || isNaN(lon)) return;

      const key = `${entry.city}|${entry.country}|${lat.toFixed(2)},${lon.toFixed(2)}`;
      if (!locations[key]) {
        locations[key] = { city: entry.city, country: entry.country, lat, lon, count: 0 };
      }
      locations[key].count++;
    });

    Object.values(locations).forEach(loc => {
      new google.maps.Marker({
        position: { lat: loc.lat, lng: loc.lon },
        map,
        title: `${loc.city}, ${loc.country} (${loc.count} visits)`,
        icon: {
          path: google.maps.SymbolPath.CIRCLE,
          scale: Math.min(5 + Math.log(loc.count) * 3, 15),
          fillColor: "#e74c3c",
          fillOpacity: 0.7,
          strokeColor: "#c0392b",
          strokeWeight: 1
        }
      });
    });
  }

  window.initMap = initMap;

  function showMapError() {
    const el = document.getElementById('map-error');
    if (el) el.style.display = 'flex';
  }

  function loadGoogleMaps() {
    if (!MAPS_API_KEY) {
      console.error('Google Maps API key is missing.');
      return showMapError();
    }

    const script = document.createElement('script');
    script.src = `https://maps.googleapis.com/maps/api/js?key=${MAPS_API_KEY}&callback=initMap`;
    script.async = true;
    script.defer = true;
    script.onerror = showMapError;
    document.head.appendChild(script);
  }

  document.addEventListener('DOMContentLoaded', loadGoogleMaps);
</script>

<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
