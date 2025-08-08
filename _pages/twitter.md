---
layout: archive
title: Tweets
stylesheet: tweets.css
permalink: /twitter/
pagination:
  enabled: true
  collection: all
  per_page: 5
  permalink: '/page/:num/'
  sort_field: 'date'
  sort_reverse: true
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

{% assign posts = site.data.tweets | sort: 'date' | reverse %}

<div class="tweet-feed">
  {% for post in posts limit: paginator.per_page offset: paginator.offset %}
    {% include tweet.html post=post %}
  {% endfor %}
</div>

{% include pagination.html %}

<script>
// Client-side pagination fallback
document.addEventListener('DOMContentLoaded', function() {
  const urlParams = new URLSearchParams(window.location.search);
  const page = parseInt(urlParams.get('page')) || 1;
  
  if(page > 1) {
    const posts = document.querySelectorAll('.tweet');
    const postsPerPage = 5;
    const startIdx = (page - 1) * postsPerPage;
    
    posts.forEach((post, idx) => {
      if(idx < startIdx || idx >= startIdx + postsPerPage) {
        post.style.display = 'none';
      }
    });
  }
});
</script>
