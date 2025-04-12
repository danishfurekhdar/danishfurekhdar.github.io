---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<div class="visitor-map-container" style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px;">

# 🌍 Visitor Activity Map

### 📍 Real-Time Visitor Locations
```mermaid
pie showData
    title Visitors by Country
    {% assign countries = site.data.visitors | group_by: "country" %}
    {% for country in countries %}
    "{{ country.name }}" : {{ country.size }}
    {% endfor %}
```

### 🏙 Top Visitor Cities
<div class="city-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
{% assign cities = site.data.visitors | group_by: "city" | sort: "size" | reverse %}
{% for city in cities limit: 8 %}
    <div class="city-card" style="background: white; border-radius: 12px; padding: 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: transform 0.3s ease;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
            <span style="font-size: 28px;">🌐</span>
            <div>
                <h3 style="margin: 0; color: #2c3e50;">{{ city.name }}</h3>
                <p style="margin: 3px 0 0; color: #7f8c8d; font-size: 0.9em;">{{ city.items[0].country }}</p>
            </div>
        </div>
        <div style="border-top: 1px solid #eee; padding-top: 12px;">
            <p style="margin: 8px 0; color: #555; font-size: 0.95em;">
                <span style="display: inline-block; width: 100px;">Visits:</span>
                <strong>{{ city.size }}</strong>
            </p>
            <p style="margin: 8px 0; color: #555; font-size: 0.95em;">
                <span style="display: inline-block; width: 100px;">Coordinates:</span>
                <code>{{ city.items[0].loc }}</code>
            </p>
            <p style="margin: 8px 0 0; color: #555; font-size: 0.95em;">
                <span style="display: inline-block; width: 100px;">Last seen:</span>
                {{ city.items.last.timestamp | date: "%b %d, %Y %H:%M" }}
            </p>
        </div>
    </div>
{% endfor %}
</div>

### 📊 Visitor Statistics
<div class="stats-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; text-align: center; margin: 30px 0;">
    <div class="stat-card" style="background: #f8f9fa; border-radius: 10px; padding: 20px;">
        <div style="font-size: 2.5em; margin-bottom: 10px;">🌎</div>
        <h3 style="margin: 0 0 5px; color: #2c3e50;">Unique Countries</h3>
        <p style="font-size: 1.8em; margin: 0; font-weight: bold; color: #3498db;">
            {{ site.data.visitors | group_by: "country" | size }}
        </p>
    </div>
    <div class="stat-card" style="background: #f8f9fa; border-radius: 10px; padding: 20px;">
        <div style="font-size: 2.5em; margin-bottom: 10px;">👤</div>
        <h3 style="margin: 0 0 5px; color: #2c3e50;">Unique Visitors</h3>
        <p style="font-size: 1.8em; margin: 0; font-weight: bold; color: #e74c3c;">
            {{ site.data.visitors | group_by: "ip" | size }}
        </p>
    </div>
    <div class="stat-card" style="background: #f8f9fa; border-radius: 10px; padding: 20px;">
        <div style="font-size: 2.5em; margin-bottom: 10px;">📈</div>
        <h3 style="margin: 0 0 5px; color: #2c3e50;">Total Visits</h3>
        <p style="font-size: 1.8em; margin: 0; font-weight: bold; color: #2ecc71;">
            {{ site.data.visitors.size }}
        </p>
    </div>
</div>

</div>

<style>
.city-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
}
.stat-card {
    transition: all 0.3s ease;
}
.stat-card:hover {
    transform: scale(1.03);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
@media (max-width: 768px) {
    .city-grid, .stats-grid {
        grid-template-columns: 1fr;
    }
}
</style>
```
