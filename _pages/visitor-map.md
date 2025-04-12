---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<div class="visitor-map-container" style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px;">

# 🌍 Visitor Activity Map

### 📍 Real-Time Visitor Locations
```mermaid
pie title Visitors by Country
    {% assign countries = site.data.visitors | group_by: "country" %}
    {% for country in countries %}"{{ country.name }}" : {{ country.size }}
    {% endfor %}
```

### 🏙 Top Visitor Cities
<div class="city-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
{% assign cities = site.data.visitors | group_by: "city" | sort: "size" | reverse %}
{% for city in cities limit: 8 %}
    <div class="city-card" style="background: white; border-radius: 12px; padding: 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
            <span style="font-size: 28px;">🌐</span>
            <div>
                <h3 style="margin: 0; color: #2c3e50;">{{ city.name }}</h3>
                <p style="margin: 3px 0 0; color: #7f8c8d; font-size: 0.9em;">{{ city.items[0].country }}</p>
            </div>
        </div>
        <div style="border-top: 1px solid #eee; padding-top: 12px;">
            <p style="margin: 8px 0; color: #555;">
                <span style="display: inline-block; width: 80px;">Visits:</span>
                <strong>{{ city.size }}</strong>
            </p>
            <p style="margin: 8px 0; color: #555;">
                <span style="display: inline-block; width: 80px;">Coordinates:</span>
                <code>{{ city.items[0].loc }}</code>
            </p>
            <p style="margin: 8px 0 0; color: #555;">
                <span style="display: inline-block; width: 80px;">Last seen:</span>
                {{ city.items.last.timestamp | date: "%b %d, %Y" }}
            </p>
        </div>
    </div>
{% endfor %}
</div>

### 📊 Visitor Statistics
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 30px 0;">
    <div style="background: #f0f8ff; border-radius: 10px; padding: 15px; text-align: center;">
        <div style="font-size: 2em; margin-bottom: 5px;">🌎</div>
        <h3 style="margin: 0 0 5px;">Countries</h3>
        <p style="font-size: 1.5em; margin: 0; font-weight: bold;">
            {{ site.data.visitors | group_by: "country" | size }}
        </p>
    </div>
    <div style="background: #fff0f5; border-radius: 10px; padding: 15px; text-align: center;">
        <div style="font-size: 2em; margin-bottom: 5px;">👤</div>
        <h3 style="margin: 0 0 5px;">Unique IPs</h3>
        <p style="font-size: 1.5em; margin: 0; font-weight: bold;">
            {{ site.data.visitors | group_by: "ip" | size }}
        </p>
    </div>
    <div style="background: #f0fff0; border-radius: 10px; padding: 15px; text-align: center;">
        <div style="font-size: 2em; margin-bottom: 5px;">📈</div>
        <h3 style="margin: 0 0 5px;">Total Visits</h3>
        <p style="font-size: 1.5em; margin: 0; font-weight: bold;">
            {{ site.data.visitors.size }}
        </p>
    </div>
</div>

</div>
