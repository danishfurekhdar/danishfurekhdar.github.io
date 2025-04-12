---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

## Visitor Locations Around the World

<div id="visitor-map" style="height: 600px; width: 100%; border: 1px solid #ccc; margin-bottom: 20px;"></div>

<!-- Load Leaflet CSS first -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
      integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
      crossorigin=""/>

<!-- Load Marker Cluster CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.css"/>
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.Default.css"/>

<!-- Load Leaflet JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
        integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
        crossorigin=""></script>

<!-- Load Marker Cluster JS -->
<script src="https://unpkg.com/leaflet.markercluster@1.4.1/dist/leaflet.markercluster.js"></script>

<script>
// Wait for the page to fully load before initializing the map
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map centered on the world
    const map = L.map('visitor-map').setView([20, 0], 2);
    
    // Add OpenStreetMap tiles with proper attribution
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(map);
    
    // Sample visitor data - replace with your actual data
    const visitors = [
        {country: "United States", lat: 39.8283, lng: -98.5795, count: 152},
        {country: "United Kingdom", lat: 54.7024, lng: -3.2766, count: 87},
        {country: "Germany", lat: 51.1657, lng: 10.4515, count: 64},
        {country: "Japan", lat: 36.5748, lng: 139.2394, count: 42},
        {country: "Brazil", lat: -10.3333, lng: -53.2, count: 38},
        {country: "India", lat: 22.3511, lng: 78.6677, count: 72},
        {country: "Australia", lat: -24.7761, lng: 134.755, count: 29},
        {country: "Canada", lat: 61.0667, lng: -107.9917, count: 53},
        {country: "France", lat: 46.6031, lng: 1.8883, count: 47},
        {country: "South Africa", lat: -28.4793, lng: 24.6727, count: 18}
    ];
    
    // Create marker cluster group
    const markers = L.markerClusterGroup();
    
    // Add circle markers for each country
    visitors.forEach(visitor => {
        const marker = L.circleMarker([visitor.lat, visitor.lng], {
            radius: 5 + (visitor.count / 10), // Size based on visitor count
            fillColor: "#3388ff",
            color: "#000",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
        }).bindPopup(`<b>${visitor.country}</b><br>Visitors: ${visitor.count}`);
        
        markers.addLayer(marker);
    });
    
    // Add markers to the map
    map.addLayer(markers);
    
    // Add a note if the map doesn't display
    if (!map.getContainer().querySelector('.leaflet-tile')) {
        const errorDiv = document.createElement('div');
        errorDiv.style.color = 'red';
        errorDiv.style.padding = '20px';
        errorDiv.style.textAlign = 'center';
        errorDiv.innerHTML = 'Map failed to load. Please check your internet connection.';
        map.getContainer().appendChild(errorDiv);
    }
});
</script>

<p>This map shows visitors to our website from around the world.</p>
