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
(function() {
  // Liquid-safe count (becomes a number at build time; falls back to 0 if missing)
  var TWEET_COUNT = {{ tweets.size | default: 0 }};
  console.log("Total tweets:", TWEET_COUNT);

  var container = document.getElementById('tweet-container');
  var tweets = Array.prototype.slice.call(container.querySelectorAll('.tweet'));
  if (!tweets.length) return;

  var tweetsPerPage = 5;
  var currentPage = 1;
  var totalPages = Math.max(1, Math.ceil(tweets.length / tweetsPerPage));

  function showPage(page) {
    // Clamp page
    page = Math.max(1, Math.min(totalPages, page));

    // Hide all
    tweets.forEach(function(el) { el.classList.add('is-hidden'); });

    // Show current slice
    var start = (page - 1) * tweetsPerPage;
    var end = Math.min(start + tweetsPerPage, tweets.length);
    for (var i = start; i < end; i++) {
      tweets[i].classList.remove('is-hidden');
    }

    // Update UI
    document.getElementById('page-info').textContent = 'Page ' + page + ' of ' + totalPages;
    document.getElementById('prev-btn').disabled = (page <= 1);
    document.getElementById('next-btn').disabled = (page >= totalPages);

    currentPage = page;
  }

  document.getElementById('prev-btn').addEventListener('click', function() {
    showPage(currentPage - 1);
  });
  document.getElementById('next-btn').addEventListener('click', function() {
    showPage(currentPage + 1);
  });

  // Initial render: if JS runs, paginate; otherwise all tweets are visible.
  showPage(1);
})();
</script>
