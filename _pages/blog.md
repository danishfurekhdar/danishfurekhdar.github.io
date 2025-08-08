---
layout: archive
title: My Blog
description: Thoughts and ideas worth sharing
permalink: /blog/
---

<div class="blog-container">
  <!-- Posts will be inserted here by Jekyll -->
  {% for post in site.data.posts %}
    {% include posts.html post=post %}
  {% endfor %}
</div>

<style>
  /* Same CSS as before */
  .blog-container {
    max-width: 600px;
    margin: 0 auto;
    font-family: sans-serif;
  }
  .post {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin: 15px 0;
    background: white;
  }
  /* Rest of your CSS */
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Like button functionality
  document.querySelectorAll('.like-button').forEach(button => {
    button.addEventListener('click', function() {
      const postId = this.dataset.postId;
      const likeCount = this.querySelector('.like-count');
      likeCount.textContent = parseInt(likeCount.textContent) + 1;
      // In a real app, you would send this to your server
      console.log(`Liked post ${postId}`);
    });
  });

  // Comment toggle functionality
  document.querySelectorAll('.comment-toggle').forEach(button => {
    button.addEventListener('click', function() {
      const postId = this.dataset.postId;
      const form = document.getElementById(`comment-form-${postId}`);
      form.style.display = form.style.display === 'none' ? 'block' : 'none';
    });
  });

  // Comment submission
  document.querySelectorAll('.comment-submit').forEach(button => {
    button.addEventListener('click', function() {
      const postId = this.closest('.comment-form').id.split('-')[2];
      const input = this.previousElementSibling;
      const content = input.value.trim();
      
      if (content) {
        const commentsContainer = document.getElementById(`comments-${postId}`);
        const newComment = document.createElement('div');
        newComment.className = 'comment';
        newComment.innerHTML = `
          <strong>@current_user</strong>
          <p>${content}</p>
          <small>Just now</small>
        `;
        commentsContainer.appendChild(newComment);
        input.value = '';
      }
    });
  });
});
</script>
