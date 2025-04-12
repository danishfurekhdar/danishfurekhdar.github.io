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
        <p>Map failed to load. Please check your internet connection.</p>
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
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: #f8d7da;
    color: #721c24;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
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

  /* ... (rest of your existing CSS remains the same) ... */
</style>

<script>
// Secure API key handling - should be set in your site's configuration
const MAPS_API_KEY = '%%GOOGLE_MAPS_API_KEY%%';

// Fallback for development
const localApiKey = (function() {
  try {
    return 'YOUR_LOCAL_DEV_KEY'; // Only for local testing - never commit this!
  } catch (e) {
    return '';
  }
})();

function initMap() {
  try {
    console.log('[Map] Initialization started');
    
    const mapElement = document.getElementById('map');
    if (!mapElement) {
      throw new Error('Map container element not found');
    }

    const center = new google.maps.LatLng(20, 0);
    const mapOptions = {
      zoom: 2,
      center: center,
      styles: [
        { featureType: "water", elementType: "geometry", stylers: [{ color: "#d4e6f4" }] },
        { featureType: "landscape", elementType: "geometry", stylers: [{ color: "#f5f5f5" }] }
      ]
    };

    const map = new google.maps.Map(mapElement, mapOptions);
    console.log('[Map] Created successfully');

    // Test marker to verify functionality
    new google.maps.Marker({
      position: center,
      map: map,
      title: "World Center",
      icon: {
        path: google.maps.SymbolPath.CIRCLE,
        scale: 8,
        fillColor: "#3498db",
        fillOpacity: 0.9,
        strokeColor: "#2980b9",
        strokeWeight: 2
      }
    });

    // Process visitor data if available
    try {
      const data = {{ site.data.visitors | jsonify }};
      if (data && Array.isArray(data)) {
        processVisitorData(map, data);
      }
    } catch (e) {
      console.warn('[Map] Error processing visitor data:', e);
    }

  } catch (error) {
    console.error('[Map] Initialization failed:', error);
    showMapError();
  }
}

function processVisitorData(map, data) {
  const locations = {};
  let validEntries = 0;

  data.forEach(entry => {
    if (!entry.loc || !entry.city || !entry.country) return;
    
    const [latStr, lngStr] = entry.loc.split(',');
    const lat = parseFloat(latStr);
    const lng = parseFloat(lngStr);
    
    if (isNaN(lat) || isNaN(lng)) return;
    
    const locationKey = `${lat.toFixed(2)},${lng.toFixed(2)}`;
    if (!locations[locationKey]) {
      locations[locationKey] = {
        position: { lat, lng },
        city: entry.city,
        country: entry.country,
        count: 0
      };
    }
    locations[locationKey].count++;
    validEntries++;
  });

  console.log(`[Map] Processed ${validEntries} valid locations from ${data.length} entries`);

  Object.values(locations).forEach(location => {
    const markerSize = Math.min(5 + Math.log(location.count) * 3, 15);
    
    new google.maps.Marker({
      position: location.position,
      map: map,
      title: `${location.city}, ${location.country} (${location.count} visits)`,
      icon: {
        path: google.maps.SymbolPath.CIRCLE,
        scale: markerSize,
        fillColor: "#e74c3c",
        fillOpacity: 0.7,
        strokeColor: "#c0392b",
        strokeWeight: 1
      }
    });
  });
}

function showMapError() {
  const errorElement = document.getElementById('map-error');
  if (errorElement) {
    errorElement.style.display = 'flex';
  }
}

function checkGoogleMapsLoaded() {
  if (typeof google === 'undefined' || typeof google.maps === 'undefined') {
    showMapError();
    return false;
  }
  return true;
}

// Load the API safely
function loadGoogleMaps() {
  const apiKey = MAPS_API_KEY || localApiKey;
  if (!apiKey) {
    console.error('Google Maps API key not configured');
    showMapError();
    return;
  }

  const script = document.createElement('script');
  script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&callback=initMap`;
  script.async = true;
  script.defer = true;
  script.onerror = showMapError;
  document.head.appendChild(script);
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
  if (!checkGoogleMapsLoaded()) {
    loadGoogleMaps();
  }
});
</script>

<!-- Load Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
