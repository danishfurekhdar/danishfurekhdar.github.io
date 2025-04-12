---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<div style="font-family: 'Segoe UI', sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px;">
  <h1>🌍 Visitor Map (Google Maps)</h1>
  <div id="map" style="height: 500px; border-radius: 8px; margin-bottom: 30px;"></div>

  <h2>📈 Statistics</h2>
  <p>Total visits: <strong>{{ site.data.visitors | size }}</strong></p>
  <p>Unique visitors: <strong>{{ site.data.visitors | group_by: "ip" | size }}</strong></p>
</div>

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

<!-- Replace YOUR_API_KEY below with your actual API key -->
<script async
  src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAT67_M0K-_BKk8hXRfFIA1ewg6_2WxlCU&callback=initMap">
</script>
