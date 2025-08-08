---
layout: archive
title: Tweets
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

<div id="tweet-container">
  <!-- Debug: First check if tweets exist -->
  {% if site.data.tweets.size > 0 %}
    {% for post in site.data.tweets %}
      <div class="tweet" style="display:none; border:1px solid #ddd; padding:15px; margin-bottom:20px;">
        <strong>@{{ post.author }}</strong> · {{ post.date | date: "%b %d, %Y" }}
        <p>{{ post.content }}</p>
        {% if post.image %}
          <img src="{{ post.image }}" style="max-width:100%; border-radius:15px;">
        {% endif %}
      </div>
    {% endfor %}
  {% else %}
    <p>No tweets found. Check _data/tweets.yml</p>
  {% endif %}
</div>

<div class="pagination" style="text-align:center; margin:30px 0;">
  <button id="prev-btn" disabled style="background:#1da1f2; color:white; border:none; padding:8px 16px; border-radius:20px;">← Newer</button>
  <span id="page-info" style="margin:0 15px;">Page 1</span>
  <button id="next-btn" style="background:#1da1f2; color:white; border:none; padding:8px 16px; border-radius:20px;">Older →</button>
</div>

<script>
// Simple debug check
console.log("Total tweets:", {{ site.data.tweets.size }});

document.addEventListener('DOMContentLoaded', function() {
  const tweets = document.querySelectorAll('.tweet');
  const tweetsPerPage = 5;
  let currentPage = 1;
  
  function showPage(page) {
    // First verify we have tweets
    if(tweets.length === 0) {
      console.error("No tweets found in DOM");
      return;
    }
    
    // Hide all
    tweets.forEach(post => post.style.display = 'none');
    
    // Show current page
    const start = (page - 1) * tweetsPerPage;
    const end = start + tweetsPerPage;
    for(let i = start; i < end && i < tweets.length; i++) {
      tweets[i].style.display = 'block';
    }
    
    // Update UI
    document.getElementById('page-info').textContent = 
      `Page ${page} of ${Math.ceil(tweets.length / tweetsPerPage)}`;
    document.getElementById('prev-btn').disabled = page <= 1;
    document.getElementById('next-btn').disabled = page >= Math.ceil(tweets.length / tweetsPerPage);
  }

  // Button handlers
  document.getElementById('prev-btn').addEventListener('click', () => {
    if(currentPage > 1) showPage(--currentPage);
  });
  
  document.getElementById('next-btn').addEventListener('click', () => {
    if(currentPage < Math.ceil(tweets.length / tweetsPerPage)) showPage(++currentPage);
  });

  // Initial load
  showPage(1);
});
</script>
