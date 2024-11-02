from .models import Post, Comment 
from django import forms


class PostForm(forms.ModelForm):
  class Meta:
    model = Post 
    fields = ['title', 'content', 'category']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['author_name', 'content']