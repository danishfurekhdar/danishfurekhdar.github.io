---
layout: archive
title: Tweets
stylesheet: tweets.css
permalink: /twitter/
pagination:
  enabled: true
  collection: posts
  per_page: 5
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

<div class="tweet-feed">
  {% for post in paginator.posts %}
    {% include tweet.html post=post %}
  {% endfor %}
</div>

<!-- Pagination controls -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}" class="previous">← Newer</a>
  {% endif %}
  
  <span class="page-number">
    Page {{ paginator.page }} of {{ paginator.total_pages }}
  </span>
  
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}" class="next">Older →</a>
  {% endif %}
</div>

<!-- Optional: Add some styling for pagination -->
<style>
.pagination {
  text-align: center;
  margin: 30px 0;
  font-size: 1.1em;
}

.pagination a, .page-number {
  margin: 0 10px;
  text-decoration: none;
  color: #1da1f2;
}

.pagination a:hover {
  text-decoration: underline;
}
</style>
