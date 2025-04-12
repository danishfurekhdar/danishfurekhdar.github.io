---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

## Visitor Locations Around the World

<div id="visitor-map" style="height: 600px; width: 100%; margin-bottom: 20px;"></div>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.css" />
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.Default.css" />

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet.markercluster@1.4.1/dist/leaflet.markercluster.js"></script>

<script>
// Visitor data - in a real implementation, this would come from your analytics
const visitorData = [
    { country: "United States", lat: 37.0902, lng: -95.7129, count: 125 },
    { country: "United Kingdom", lat: 55.3781, lng: -3.4360, count: 87 },
    { country: "Germany", lat: 51.1657, lng: 10.4515, count: 64 },
    { country: "Japan", lat: 36.2048, lng: 138.2529, count: 42 },
    { country: "Brazil", lat: -14.2350, lng: -51.9253, count: 38 },
    { country: "India", lat: 20.5937, lng: 78.9629, count: 72 },
    { country: "Australia", lat: -25.2744, lng: 133.7751, count: 29 },
    { country: "Canada", lat: 56.1304, lng: -106.3468, count: 53 },
    { country: "France", lat: 46.2276, lng: 2.2137, count: 47 },
    { country: "South Africa", lat: -30.5595, lng: 22.9375, count: 18 }
];

// Initialize the map
const map = L.map('visitor-map').setView([20, 0], 2);

// Add tile layer (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Create marker cluster group
const markers = L.markerClusterGroup();

// Add markers for each country
visitorData.forEach(visitor => {
    const marker = L.marker([visitor.lat, visitor.lng]);
    marker.bindPopup(`<b>${visitor.country}</b><br>Visitors: ${visitor.count}`);
    markers.addLayer(marker);
});

// Add markers to map
map.addLayer(markers);
</script>
