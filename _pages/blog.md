---
layout: archive
title: My Blog
description: Thoughts and ideas worth sharing
permalink: /blog/
---

{% raw %}
{% assign post = site.data.post_data.current_post %}
{% endraw %}

# {{ page.title }}

![Featured Image]({% raw %}{{ post.feature_image }}{% endraw %})  
*Caption: {% raw %}{{ post.image_caption }}{% endraw %}*

## Dynamic Statistics

<div class="post-stats">
  <div class="stat-item">
    <span class="stat-value" id="viewCount">{% raw %}{{ post.stats.views }}{% endraw %}</span>
    <span class="stat-label">Views</span>
  </div>
  <div class="stat-item">
    <span class="stat-value" id="likeCount">{% raw %}{{ post.stats.likes }}{% endraw %}</span>
    <span class="stat-label">Likes</span>
    <button class="like-button" onclick="incrementLike()">❤️ Like</button>
  </div>
  <div class="stat-item">
    <span class="stat-value">{% raw %}{{ post.stats.shares }}{% endraw %}</span>
    <span class="stat-label">Shares</span>
  </div>
</div>

## Recent Comments

<div class="comment-search">
  <input type="text" id="commentSearch" placeholder="Search comments...">
</div>

<div class="comments-section">
  {% raw %}{% for comment in post.comments %}{% endraw %}
  <div class="comment">
    <strong>{% raw %}{{ comment.author }}{% endraw %}</strong>
    <small>{% raw %}{{ comment.date }}{% endraw %}</small>
    <p>{% raw %}{{ comment.text }}{% endraw %}</p>
  </div>
  {% raw %}{% endfor %}{% endraw %}
</div>

## Engagement Chart

<canvas id="engagementChart" width="400" height="200"></canvas>

<script>
// Like button functionality
function incrementLike() {
  const likeCount = document.getElementById('likeCount');
  let currentLikes = parseInt(likeCount.textContent);
  likeCount.textContent = currentLikes + 1;
  
  // In a real implementation, you would send this to a server
  // For Jekyll, you might use a static forms service or GitHub API
  console.log('Like recorded!');
}

// Comment search functionality
document.getElementById('commentSearch').addEventListener('input', function(e) {
  const searchTerm = e.target.value.toLowerCase();
  const comments = document.querySelectorAll('.comment');
  
  comments.forEach(comment => {
    const text = comment.textContent.toLowerCase();
    if (text.includes(searchTerm)) {
      comment.style.display = 'block';
    } else {
      comment.style.display = 'none';
    }
  });
});

// Chart.js implementation
document.addEventListener('DOMContentLoaded', function() {
  const ctx = document.getElementById('engagementChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Views', 'Likes', 'Shares'],
      datasets: [{
        label: 'Post Engagement',
        data: [
          {% raw %}{{ post.stats.views }}{% endraw %}, 
          {% raw %}{{ post.stats.likes }}{% endraw %}, 
          {% raw %}{{ post.stats.shares }}{% endraw %}
        ],
        backgroundColor: [
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 99, 132, 0.6)',
          'rgba(75, 192, 192, 0.6)'
        ],
        borderColor: [
          'rgba(54, 162, 235, 1)',
          'rgba(255, 99, 132, 1)',
          'rgba(75, 192, 192, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});
</script>

<style>
.post-stats {
  display: flex;
  gap: 2rem;
  margin: 2rem 0;
}

.stat-item {
  text-align: center;
}

.stat-value {
  display: block;
  font-size: 2rem;
  font-weight: bold;
}

.like-button {
  margin-top: 0.5rem;
  padding: 0.25rem 0.5rem;
  background: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
}

.comment-search {
  margin: 1rem 0;
}

.comment-search input {
  width: 100%;
  padding: 0.5rem;
}

.comment {
  border: 1px solid #eee;
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 4px;
}
</style>
