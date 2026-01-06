---
layout: single
title: Curriculum Vitae
permalink: /cv/
author_profile: true
---


<link rel="stylesheet" href="{{ '/assets/css/cv.css' | relative_url }}">

# {{ site.data.cv.basics.name }}

**{{ site.data.cv.basics.location }}**  
📞 {{ site.data.cv.basics.phone }} · ✉️ {{ site.data.cv.basics.email }}

---

## Research Profile

{{ site.data.cv.basics.summary }}

---

## Education

{% for edu in site.data.cv.education %}
### {{ edu.degree }}
**{{ edu.institution }}, {{ edu.location }}**  
*{{ edu.years }}*

{% for d in edu.details %}
- {{ d }}
{% endfor %}

{% endfor %}

---

## Academic Appointments

{% for job in site.data.cv.appointments %}
### {{ job.title }}
**{{ job.institution }}, {{ job.location }}**  
*{{ job.years }}*  

- {{ job.description }}
- Advisor: {{ job.advisor }}

{% endfor %}

---

## Research Training & Internships

{% for t in site.data.cv.training %}
### {{ t.title }}
**{{ t.institution }}, {{ t.location }}**  
*{{ t.years }}*  

- {{ t.topic }}
- Advisor: {{ t.advisor }}

{% endfor %}

---

## Skills

**Languages:** {{ site.data.cv.skills.languages | join: ", " }}

**Scientific Computing:** {{ site.data.cv.skills.computing | join: ", " }}

**Software:** {{ site.data.cv.skills.software | join: ", " }}

**Operating Systems:** {{ site.data.cv.skills.os | join: ", " }}

---

## Honors & Awards

{% for a in site.data.cv.awards %}
- {{ a }}
{% endfor %}

---

## Professional Service

{% for s in site.data.cv.service %}
- {{ s }}
{% endfor %}

---

## Teaching Experience

{% for t in site.data.cv.teaching %}
- **{{ t.course }}**, {{ t.role }}  
  {{ t.institution }} ({{ t.years }})
{% endfor %}

---

## Research Activities

{% for act in site.data.cv.activities %}
- {{ act }}
{% endfor %}
