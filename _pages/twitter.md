---
layout: archive
title: Tweets
stylesheet: tweets.css
permalink: /twitter/
---

<div class="twitter-feed">
  {% for tweet in site.data.tweets %}
    {% include tweet.html tweet=tweet %}
  {% endfor %}
</div>

<!-- New Tweet Composition (client-side only) -->
<div class="tweet-composer">
  <div class="composer-header">
    <img class="composer-avatar" src="/assets/images/avatars/you.jpg" alt="Your avatar">
    <textarea placeholder="What's happening?"></textarea>
  </div>
  <div class="composer-footer">
    <div class="composer-actions">
      <button class="media-btn">
        <svg viewBox="0 0 24 24"><g><path d="M3 5.5C3 4.119 4.119 3 5.5 3h13C19.881 3 21 4.119 21 5.5v13c0 1.381-1.119 2.5-2.5 2.5h-13C4.119 21 3 19.881 3 18.5v-13zM5.5 5c-.276 0-.5.224-.5.5v9.086l3-3 3 3 5-5 3 3V5.5c0-.276-.224-.5-.5-.5h-13zM19 15.414l-3-3-5 5-3-3-3 3V18.5c0 .276.224.5.5.5h13c.276 0 .5-.224.5-.5v-3.086zM9.75 7C8.784 7 8 7.784 8 8.75s.784 1.75 1.75 1.75 1.75-.784 1.75-1.75S10.716 7 9.75 7z"></path></g></svg>
      </button>
    </div>
    <button class="tweet-btn" disabled>Tweet</button>
  </div>
</div>

<style>
.tweet-composer {
  padding: 12px 16px;
  border-bottom: 1px solid #e6ecf0;
  
  .composer-header {
    display: flex;
    gap: 12px;
  }
  
  .composer-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    object-fit: cover;
  }
  
  textarea {
    flex: 1;
    border: none;
    resize: none;
    font-size: 1.2em;
    min-height: 60px;
    padding: 12px 0;
    
    &:focus {
      outline: none;
    }
    
    &::placeholder {
      color: #536471;
    }
  }
  
  .composer-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 12px;
    border-top: 1px solid #e6ecf0;
  }
  
  .composer-actions {
    display: flex;
    gap: 4px;
  }
  
  .media-btn {
    background: none;
    border: none;
    color: #1d9bf0;
    padding: 8px;
    border-radius: 9999px;
    cursor: pointer;
    
    svg {
      width: 20px;
      height: 20px;
      fill: currentColor;
    }
    
    &:hover {
      background: rgba(29, 155, 240, 0.1);
    }
  }
  
  .tweet-btn {
    background: #1d9bf0;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 9999px;
    font-weight: 700;
    cursor: pointer;
    opacity: 0.5;
    
    &:not(:disabled) {
      opacity: 1;
    }
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const textarea = document.querySelector('.tweet-composer textarea');
  const tweetBtn = document.querySelector('.tweet-btn');
  
  textarea.addEventListener('input', function() {
    tweetBtn.disabled = this.value.trim().length === 0;
  });
  
  // In a real implementation, you would handle form submission here
  tweetBtn.addEventListener('click', function() {
    alert('In a real implementation, this would post a new tweet');
  });
});
</script>
