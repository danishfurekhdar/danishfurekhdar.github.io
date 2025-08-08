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

<div class="tweet-feed">
  {% for post in site.data.tweets %}
    {% include tweet.html post=post %}
  {% endfor %}
</div>

<!-- Optional: New post form for demonstration -->
<div class="tweet" style="background: #f5f8fa;">
  <div class="tweet-header">
    <img class="tweet-avatar" src="/assets/images/avatars/you.jpg" alt="Your name">
    <div style="flex: 1;">
      <textarea placeholder="What's happening?" style="width: 100%; border: none; background: transparent; resize: none; font-size: 1.1em; padding: 10px 0; min-height: 60px;"></textarea>
    </div>
  </div>
  <button style="float: right; background: #1da1f2; color: white; border: none; padding: 8px 16px; border-radius: 20px; font-weight: bold;">Post</button>
  <div style="clear: both;"></div>
</div>
