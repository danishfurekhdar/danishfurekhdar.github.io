---
layout: archive
title: "Tweets"
permalink: /twitter/
---

<style>
/* ---------- Global container ---------- */
#tweet-container {
  max-width: 700px;
  margin: 0 auto;
}

/* ---------- Tweet Card ---------- */
.tweet {
  padding: 18px 20px;
  margin: 0 auto 22px;
  background: #ffffff;
  border: 1px solid #e1e8ed;
  border-radius: 14px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.tweet:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* ---------- Header ---------- */
.tweet-header {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
}

.tweet-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 12px;
  border: 1px solid #ccd6dd;
}

.tweet-author {
  flex: 1;
}

.tweet-name {
  font-weight: 700;
  font-size: 1.05em;
  color: #14171a;
}

.tweet-handle {
  color: #657786;
  font-size: 0.9em;
}

.tweet-date {
  color: #657786;
  font-size: 0.85em;
  white-space: nowrap;
}

/* ---------- Content ---------- */
.tweet-content {
  margin-top: 8px;
  font-size: 1.05em;
  line-height: 1.5;
  color: #14171a;
}

/* ---------- Image Preview ---------- */
.tweet-media {
  margin-top: 16px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #e1e8ed;
}

.tweet-media img {
  width: 100%;
  height: auto;
  display: block;
}

/* ---------- Pagination ---------- */
.pagination {
  text-align: center;
  margin: 35px 0;
}

.pagination button {
  background: #1da1f2;
  color: #fff;
  border: none;
  padding: 10px 18px;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 600;
  margin: 0 10px;
  transition: background 0.15s ease;
}

.pagination button:disabled {
  background: #a0d4f8;
  cursor: not-allowed;
}

.pagination button:hover:not(:disabled) {
  background: #0d8bda;
}

#page-info {
  font-weight: 600;
  color: #555;
}

/* ---------- Mobile adjustments ---------- */
@media (max-width: 500px) {
  .tweet-header {
    flex-wrap: wrap;
  }
  .tweet-date {
    width: 100%;
    text-align: right;
    margin-top: 4px;
  }
}
</style>

{% assign tweets_src = site.data.tweets | default: empty %}
{% assign tweets = tweets_src | values %}

<div id="tweet-container">
  {% if tweets and tweets.size > 0 %}
    {% for post in tweets %}
      <div class="tweet">
        <div class="tweet-header">
          {% if post.avatar %}
            <img class="tweet-avatar" src="{{ post.avatar }}" alt="{{ post.name | default: post.handle | default: 'Avatar' }}">
          {% endif %}
          <div class="tweet-author">
            <span class="tweet-name">{{ post.name | default: post.author | default: post.handle | default: "Unknown" }}</span><br>
            {% if post.handle %}
              <span class="tweet-handle">@{{ post.handle }}</span>
            {% endif %}
          </div>
          {% if post.date %}
            <div class="tweet-date">{{ post.date | date: "%b %d, %Y" }}</div>
          {% endif %}
        </div>

        {% if post.content %}
          <div class="tweet-content">{{ post.content | markdownify }}</div>
        {% endif %}

        {% if post.image %}
          <div class="tweet-media">
            <img src="{{ post.image }}" alt="Tweet image">
          </div>
        {% endif %}
      </div>
    {% endfor %}
  {% else %}
    <p>No tweets found. Create a <code>_data/tweets.yml</code> file with a list of tweets.</p>
  {% endif %}
</div>

<!-- ------------ Pagination UI ------------ -->
<div class="pagination">
  <button id="prev-btn" disabled>← Newer</button>
  <span id="page-info">Page 1</span>
  <button id="next-btn">Older →</button>
</div>

<noscript>
  <p style="text-align:center; color:#657786;">
    JavaScript disabled — showing all tweets.
  </p>
</noscript>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var tweets = Array.from(document.querySelectorAll('.tweet'));
  if (!tweets.length) return;

  var perPage = 4;
  var currentPage = 1;
  var totalPages = Math.ceil(tweets.length / perPage);

  var prevBtn = document.getElementById('prev-btn');
  var nextBtn = document.getElementById('next-btn');
  var pageInfo = document.getElementById('page-info');
  var pagination = document.querySelector('.pagination');

  function renderPage(page) {
    page = Math.max(1, Math.min(page, totalPages));

    tweets.forEach(function (tweet, i) {
      tweet.style.display = (i >= (page-1)*perPage && i < page*perPage)
        ? 'block'
        : 'none';
    });

    prevBtn.disabled = (page === 1);
    nextBtn.disabled = (page === totalPages);
    pageInfo.textContent = "Page " + page + " of " + totalPages;

    currentPage = page;

    if (totalPages <= 1) pagination.style.display = 'none';
  }

  prevBtn.addEventListener('click', () => renderPage(currentPage - 1));
  nextBtn.addEventListener('click', () => renderPage(currentPage + 1));

  renderPage(1);
});
</script>
