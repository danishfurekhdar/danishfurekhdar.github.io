---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

## Visitor Locations Around the World

<div id="visitor-map" style="height: 600px; width: 100%; border: 1px solid #ccc; background: #f0f0f0; display: flex; justify-content: center; align-items: center;">
    <div id="map-loading">Loading world map...</div>
</div>

<!-- Load Leaflet from CDN with fallback -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const mapContainer = document.getElementById('visitor-map');
    const loadingMessage = document.getElementById('map-loading');
    
    // Check if Leaflet loaded properly
    if (typeof L === 'undefined') {
        loadingMessage.innerHTML = 'Error: Failed to load map library. Please try refreshing.';
        return;
    }

    try {
        // Initialize the map
        const map = L.map('visitor-map').setView([20, 0], 2);
        
        // Add tiles with error handling
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data © OpenStreetMap contributors',
            maxZoom: 18,
        }).on('tileerror', function() {
            loadingMessage.innerHTML = 'Error loading map tiles. Trying alternative source...';
            // Try a different tile source
            L.tileLayer('https://tile.openstreetmap.de/{z}/{x}/{y}.png').addTo(map);
        }).addTo(map);
        
        // Sample data - replace with your actual visitor data
        const visitors = [
            {country: "United States", lat: 39.8283, lng: -98.5795},
            {country: "United Kingdom", lat: 54.7024, lng: -3.2766},
            {country: "Germany", lat: 51.1657, lng: 10.4515}
        ];
        
        // Add markers
        visitors.forEach(visitor => {
            L.marker([visitor.lat, visitor.lng])
                .addTo(map)
                .bindPopup(visitor.country);
        });
        
        // Hide loading message when map is ready
        loadingMessage.style.display = 'none';
        
    } catch (error) {
        loadingMessage.innerHTML = 'Error initializing map: ' + error.message;
        console.error('Map initialization error:', error);
    }
});
</script>
