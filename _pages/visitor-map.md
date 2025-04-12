---
layout: archive
title: Visitor Map
permalink: /visitor-map/
---

<div style="font-family: 'Segoe UI', sans-serif; max-width: 900px; margin: 0 auto; padding: 20px;">

# 🌍 Visitor Map

### 📊 Visitor Distribution

{% assign countries = site.data.visitors | group_by: "country" %}
{% capture pie_data %}
pie title Visitors by Country
{% for country in countries %}
    "{{ country.name }}" : {{ country.size }}
{% endfor %}
{% endcapture %}

```mermaid
{{ pie_data }}
```

### 🏙 Visitor Locations

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">
{% assign cities = site.data.visitors | group_by: "city" | sort: "size" | reverse %}
{% for city in cities limit: 6 %}
<div style="background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 24px;">📍</span>
        <h3 style="margin: 0;">{{ city.name }}</h3>
    </div>
    <p style="margin: 5px 0; color: #555;">Visits: <strong>{{ city.size }}</strong></p>
    <p style="margin: 5px 0; font-size: 0.9em; color: #777;">Country: {{ city.items[0].country }}</p>
</div>
{% endfor %}
</div>

### 📈 Statistics

<div style="background: #f8f9fa; border-radius: 8px; padding: 15px; margin-top: 20px;">
    <p>Total visits: <strong>{{ site.data.visitors.size }}</strong></p>
    <p>Unique visitors: <strong>{{ site.data.visitors | group_by: "ip" | size }}</strong></p>
</div>

</div>
