---
layout: single
title: Curriculum Vitae
permalink: /cv/
author_profile: true
---


<link rel="stylesheet" href="{{ '/assets/css/cv.css' | relative_url }}">

## Research Profile
{{ site.data.cv.profile }}

## Education
{% for edu in site.data.cv.education %}
**{{ edu.degree }}**  
{{ edu.institution }}, {{ edu.location }}  
*{{ edu.years }}*  

- **Thesis:** {{ edu.thesis }}
- **Advisor:** {{ edu.advisor }}

{% if edu.focus %}
**Research Focus:**  
{% for f in edu.focus %}- {{ f }}{% endfor %}
{% endif %}

{% endfor %}

## Academic Appointments
{% for job in site.data.cv.appointments %}
**{{ job.title }}**, {{ job.institution }}  
{{ job.location }} — *{{ job.years }}*  
Advisor: {{ job.advisor }}  
{{ job.topic }}

{% endfor %}

## Publications
<ul>
{% for pub in site.data.cv.publications %}
<li>{{ pub }}</li>
{% endfor %}
</ul>

## Research Training & Internships
{% for t in site.data.cv.training %}
**{{ t.institution }}**, {{ t.location }}  
*{{ t.years }}*  
{{ t.topic }}  
Advisor: {{ t.advisor }}

{% endfor %}

## Skills
**Languages:** {{ site.data.cv.skills.languages | join: ", " }}  
**Scientific Computing:** {{ site.data.cv.skills.computing | join: ", " }}  
**Software:** {{ site.data.cv.skills.software | join: ", " }}  
**Operating Systems:** {{ site.data.cv.skills.os | join: ", " }}

## Honors & Awards
<ul>
{% for a in site.data.cv.awards %}
<li>{{ a }}</li>
{% endfor %}
</ul>

## Professional Service
<ul>
{% for s in site.data.cv.service %}
<li>{{ s }}</li>
{% endfor %}
</ul>

## Teaching
{% for t in site.data.cv.teaching %}
**{{ t.course }}**, {{ t.role }}  
{{ t.institution }} — *{{ t.years }}*

{% endfor %}
