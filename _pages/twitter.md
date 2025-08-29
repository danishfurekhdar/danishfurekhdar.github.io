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
.tweet-author { flex: 1; }
.tweet-name { font-weight: bold; display: block; }
.tweet-handle, .tweet-date { color: #657786; font-size: 0.9em; }
.tweet-content { margin: 10px 0; line-height: 1.4; font-size: 1.1em; }
.tweet-media { margin-top: 15px; border-radius: 15px; overflow: hidden; border: 1px solid #e1e8ed; }
.tweet-media img { width: 100%; height: auto; display: block; }

/* Hidden class used by JS pagination */
.is-hidden { display: none !important; }
</style>

{% assign tweets_src = site.data.tweets | default: empty %}
{% comment %}
If _data/tweets.yml is a map (key: {...}), convert to an array of values.
If it’s already a list, | values is a no-op.
{% endcomment %}
{% assign tweets = tweets_src | values %}

<div id="tweet-container">
  {% if tweets and tweets.size > 0 %}
    {% for post in tweets %}
      <div class="tweet">
        <div class="tweet-header">
          {% if post.avatar %}
            <img class="tweet-avatar" src="{{ post.avatar }}" alt="{{ post.author | default: post.handle | default: 'Author' }} avatar">
          {% endif %}
          <div class="tweet-author">
            <span class="tweet-name">{{ post.name | default: post.author | default: post.handle | default: 'Unknown' }}</span>
            {% if post.handle %}
              <span class="tweet-handle">@{{ post.handle }}</span>
            {% endif %}
          </div>
          {% if post.date %}
            <div class="tweet-date">{{ post.date | date: "%b %d, %Y" }}</div>
          {% endif %}
        </div>

        {% if post.content %}
          <div class="tweet-content">{{ post.content }}</div>
        {% endif %}

        {% if post.image %}
          <div class="tweet-media">
            <img src="{{ post.image }}" alt="Tweet media">
          </div>
        {% endif %}
      </div>
    {% endfor %}
  {% else %}
    <p>No tweets found. Make sure you have <code>_data/tweets.yml</code> with a list (or map) of tweets.</p>
  {% endif %}
</div>

<div class="pagination" style="text-align:center; margin:30px 0;">
  <button id="prev-btn" disabled style="background:#1da1f2; color:white; border:none; padding:8px 16px; border-radius:20px;">← Newer</button>
  <span id="page-info" style="margin:0 15px;">Page 1</span>
  <button id="next-btn" style="background:#1da1f2; color:white; border:none; padding:8px 16px; border-radius:20px;">Older →</button>
</div>

<noscript>
  <p style="text-align:center;color:#657786;">Pagination requires JavaScript. All tweets are shown above.</p>
</noscript>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var container = document.getElementById('tweet-container');
  if (!container) return;

  var tweets = Array.prototype.slice.call(container.querySelectorAll('.tweet'));
  if (!tweets.length) return;

  var tweetsPerPage = 4; // ← show four per page
  var currentPage = 1;
  var totalPages = Math.max(1, Math.ceil(tweets.length / tweetsPerPage));

  var prevBtn = document.getElementById('prev-btn');
  var nextBtn = document.getElementById('next-btn');
  var pageInfo = document.getElementById('page-info');

  function showPage(page) {
    page = Math.max(1, Math.min(totalPages, page));

    // Hide all
    tweets.forEach(function (el) { el.style.display = 'none'; });

    // Show slice
    var start = (page - 1) * tweetsPerPage;
    var end = Math.min(start + tweetsPerPage, tweets.length);
    for (var i = start; i < end; i++) {
      tweets[i].style.display = 'block';
    }

    // Update UI
    if (pageInfo) pageInfo.textContent = 'Page ' + page + ' of ' + totalPages;
    if (prevBtn) prevBtn.disabled = (page <= 1);
    if (nextBtn) nextBtn.disabled = (page >= totalPages);

    currentPage = page;
  }

  // Wire buttons
  if (prevBtn) prevBtn.addEventListener('click', function () { showPage(currentPage - 1); });
  if (nextBtn) nextBtn.addEventListener('click', function () { showPage(currentPage + 1); });

  // Hide pagination entirely if only one page
  var pagination = document.querySelector('.pagination');
  if (pagination && totalPages <= 1) {
    pagination.style.display = 'none';
  }

  // Initial render
  showPage(1);
});
</script>

