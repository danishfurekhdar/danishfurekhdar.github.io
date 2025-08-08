---
layout: archive
title: My Blog
description: Thoughts and ideas worth sharing
permalink: /blog/
---

{% raw %}
```html
<div class="blog-container">
  <!-- New Post Form -->
  <div class="new-post">
    <textarea id="new-post-content" placeholder="What's on your mind?" rows="3"></textarea>
    <button onclick="createPost()">Post</button>
  </div>

  <!-- Posts will be inserted here by JavaScript -->
  <div id="posts-container">
    {% for post in site.data.posts %}
      {% include posts.html post=post %}
    {% endfor %}
  </div>
</div>

<style>
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
  
  .post-header {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .post-author {
    font-weight: bold;
    margin-right: 10px;
  }
  
  .post-date {
    color: #666;
    font-size: 0.9em;
  }
  
  .post-content {
    margin: 10px 0;
    line-height: 1.4;
  }
  
  .post-actions {
    display: flex;
    gap: 15px;
    margin-top: 10px;
  }
  
  .post-actions button {
    background: none;
    border: none;
    cursor: pointer;
    color: #666;
  }
  
  .comments {
    margin-top: 15px;
    border-top: 1px solid #eee;
    padding-top: 10px;
  }
  
  .comment {
    margin: 8px 0;
    padding: 8px;
    background: #f9f9f9;
    border-radius: 4px;
  }
  
  textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    resize: vertical;
  }
  
  button {
    background: #1da1f2;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    cursor: pointer;
  }
</style>

<script>
  // This would be replaced with actual API calls in a real implementation
  function createPost() {
    const content = document.getElementById('new-post-content').value;
    if (!content) return;
    
    // In a real app, this would send to a server
    const newPost = {
      id: Date.now(),
      author: "your_username",
      content: content,
      date: new Date().toISOString(),
      likes: 0,
      comments: []
    };
    
    // Prepend to posts container
    const postsContainer = document.getElementById('posts-container');
    const postElement = createPostElement(newPost);
    postsContainer.insertBefore(postElement, postsContainer.firstChild);
    
    // Clear input
    document.getElementById('new-post-content').value = '';
  }
  
  function createPostElement(post) {
    const postElement = document.createElement('div');
    postElement.className = 'post';
    postElement.innerHTML = `
      <div class="post-header">
        <span class="post-author">@${post.author}</span>
        <span class="post-date">${formatDate(post.date)}</span>
      </div>
      <div class="post-content">${post.content}</div>
      <div class="post-actions">
        <button onclick="likePost(${post.id})">❤️ ${post.likes}</button>
        <button onclick="showCommentBox(${post.id})">💬 Comment</button>
      </div>
      <div id="comments-${post.id}" class="comments">
        ${post.comments.map(comment => `
          <div class="comment">
            <strong>@${comment.author}</strong>
            <p>${comment.content}</p>
            <small>${formatDate(comment.date)}</small>
          </div>
        `).join('')}
      </div>
      <div id="comment-form-${post.id}" style="display: none; margin-top: 10px;">
        <textarea id="comment-input-${post.id}" placeholder="Write a comment..."></textarea>
        <button onclick="addComment(${post.id})">Post Comment</button>
      </div>
    `;
    return postElement;
  }
  
  function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString();
  }
  
  function likePost(postId) {
    // In a real app, this would update the server
    console.log(`Liked post ${postId}`);
  }
  
  function showCommentBox(postId) {
    const form = document.getElementById(`comment-form-${postId}`);
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
  }
  
  function addComment(postId) {
    const commentInput = document.getElementById(`comment-input-${postId}`);
    const content = commentInput.value;
    if (!content) return;
    
    // In a real app, this would send to a server
    const newComment = {
      author: "current_user",
      content: content,
      date: new Date().toISOString()
    };
    
    const commentsContainer = document.getElementById(`comments-${postId}`);
    const commentElement = document.createElement('div');
    commentElement.className = 'comment';
    commentElement.innerHTML = `
      <strong>@${newComment.author}</strong>
      <p>${newComment.content}</p>
      <small>${formatDate(newComment.date)}</small>
    `;
    
    commentsContainer.appendChild(commentElement);
    commentInput.value = '';
  }
</script>
```
{% endraw %}
