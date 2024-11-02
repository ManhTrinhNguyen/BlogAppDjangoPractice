from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

# Category Model
class Category(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.name 

# Post Model 
class Post(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField(unique=True)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.title 
  

# Comment model 
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  author_name = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.author_name} : {self.content}'
  









