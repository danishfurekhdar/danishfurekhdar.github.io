---
layout: archive
title: Tweets
stylesheet: tweets.css
permalink: /twitter/
---

<style>
.tweet {
  max-width: 600px;
  margin: 0 auto 20px;
  padding: 15px;
  border: 1px solid #e1e8ed;
  border-radius: 10px;
  background: white;
}

.tweet-header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  position: relative;
}

.tweet-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-right: 12px;
  object-fit: cover;
}

.tweet-author {
  flex: 1;
}

.tweet-name {
  font-weight: bold;
  display: block;
}

.tweet-handle {
  color: #657786;
  font-size: 0.9em;
}

.tweet-date {
  color: #657786;
  font-size: 0.9em;
}

.tweet-content {
  margin: 10px 0;
  line-height: 1.4;
  font-size: 1.1em;
}

.tweet-media {
  margin-top: 15px;
  border-radius: 15px;
  overflow: hidden;
  border: 1px solid #e1e8ed;
}

.tweet-media img {
  width: 100%;
  height: auto;
  display: block;
}
</style>

<div class="tweet-feed" id="tweet-container">
  {% for post in site.data.tweets %}
    <div class="tweet">
      <h3>{{ post.name }}</h3>
      <p>{{ post.date | date: "%b %d, %Y" }}</p>
      <div class="content">{{ post.content }}</div>
      {% if post.image %}
        <img src="{{ post.image }}" alt="Post image" style="max-width: 100%">
      {% endif %}
    </div>
  {% endfor %}
</div>

<div class="pagination">
  <button id="prev-btn" disabled>← Newer</button>
  <span id="page-info">Page 1</span>
  <button id="next-btn">Older →</button>
</div>

<style>
  .tweet {
    border: 1px solid #ddd;
    padding: 15px;
    margin-bottom: 20px;
    display: none; /* Hidden by default */
  }
  
  .pagination {
    text-align: center;
    margin: 30px 0;
  }
  
  .pagination button {
    padding: 8px 16px;
    margin: 0 10px;
    cursor: pointer;
  }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Debugging: Verify posts are loaded
  console.log("Total posts found:", {{ site.data.tweets.size }});
  
  const postsPerPage = 5;
  const allPosts = document.querySelectorAll('.tweet');
  const totalPages = Math.ceil(allPosts.length / postsPerPage);
  let currentPage = 1;
  
  // Initialize pagination
  function showPage(page) {
    // Hide all posts
    allPosts.forEach(post => post.style.display = 'none');
    
    // Calculate range
    const start = (page - 1) * postsPerPage;
    const end = start + postsPerPage;
    
    // Show current page posts
    for (let i = start; i < end && i < allPosts.length; i++) {
      allPosts[i].style.display = 'block';
    }
    
    // Update pagination controls
    document.getElementById('page-info').textContent = `Page ${page} of ${totalPages}`;
    document.getElementById('prev-btn').disabled = page <= 1;
    document.getElementById('next-btn').disabled = page >= totalPages;
  }
  
  // Event listeners
  document.getElementById('prev-btn').addEventListener('click', () => {
    if (currentPage > 1) showPage(--currentPage);
  });
  
  document.getElementById('next-btn').addEventListener('click', () => {
    if (currentPage < totalPages) showPage(++currentPage);
  });
  
  // Show first page initially
  showPage(1);
  
  // Debug: Verify posts are selectable
  console.log("Posts in DOM:", document.querySelectorAll('.tweet').length);
});
</script>
