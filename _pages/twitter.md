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
  <pre>{{ post | inspect }}</pre>
    <div class="tweet" data-page="{{ forloop.index0 | divided_by: 5 | plus: 1 }}">
      {% include tweet.html post=post %}
    </div>
  {% endfor %}
</div>

<!-- Pagination Controls -->
<div class="pagination">
  <button id="prev-page" disabled>← Newer</button>
  <span id="page-indicator">Page 1 of {{ site.data.tweets.size | divided_by: 5.0 | ceil }}</span>
  <button id="next-page">Older →</button>
</div>

<style>
  .tweet { display: none; }
  .tweet[data-page="1"] { display: block; } /* Show first page by default */
  
  .pagination {
    text-align: center;
    margin: 20px 0;
  }
  .pagination button {
    background: #1da1f2;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    cursor: pointer;
  }
  .pagination button:disabled {
    background: #ccc;
    cursor: not-allowed;
  }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const tweets = document.querySelectorAll('.tweet');
  const prevBtn = document.getElementById('prev-page');
  const nextBtn = document.getElementById('next-page');
  const pageIndicator = document.getElementById('page-indicator');
  const postsPerPage = 5;
  let currentPage = 1;
  const totalPages = Math.ceil(tweets.length / postsPerPage);

  function updatePage() {
    // Hide all tweets
    tweets.forEach(tweet => {
      tweet.style.display = 'none';
    });
    
    // Show tweets for current page
    const startIdx = (currentPage - 1) * postsPerPage;
    const endIdx = startIdx + postsPerPage;
    
    for (let i = startIdx; i < endIdx && i < tweets.length; i++) {
      tweets[i].style.display = 'block';
    }
    
    // Update pagination controls
    pageIndicator.textContent = `Page ${currentPage} of ${totalPages}`;
    prevBtn.disabled = currentPage === 1;
    nextBtn.disabled = currentPage === totalPages;
    
    // Update URL without reload
    history.pushState(null, '', `?page=${currentPage}`);
  }

  // Initial load
  updatePage();

  // Button events
  prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
      currentPage--;
      updatePage();
    }
  });

  nextBtn.addEventListener('click', () => {
    if (currentPage < totalPages) {
      currentPage++;
      updatePage();
    }
  });

  // Handle browser back/forward
  window.addEventListener('popstate', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const page = parseInt(urlParams.get('page')) || 1;
    if (page !== currentPage) {
      currentPage = page;
      updatePage();
    }
  });
});
</script>
