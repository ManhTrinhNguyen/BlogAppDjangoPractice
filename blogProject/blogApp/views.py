from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Post 
from .forms import CommentForm , PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.

##### List view Generic and function 
class PostListView(ListView):
  model = Post
  template_name = 'blog/post_list.html'
  context_object_name = 'posts'

def posts_list(request):
  posts = Post.objects.all()
  return render(request, 'blog/post_list.html', {'posts': posts})
#####

#### List Detail View Generic and function 
class PostDetail(DetailView):
  model= Post 
  template_name = 'blog/post_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['comment_form'] = CommentForm()
    return context
  
def post_detail(request, pk):
  post = Post.objects.get(id=pk)
  return render(request, 'blog/post_detail.html', {'post': post})
####


#### Create post Generic and function 
class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post 
  form_class = PostForm 
  template_name = 'blog/post_form.html'
  success_url = '/'

  def form_valid(self, form):
    form.instance.author = self.request.user 
    return super().form_valid(form)
  
@login_required
def create_post(request):
  form = PostForm()
 
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('posts')
    
  return render(request, 'blog/post_form.html', {'form': form})
########

##### Update View 
@login_required
def update_post(request, pk): 
  post = Post.objects.get(id = pk)
  form = PostForm(instance=post)

  if request.user != post.author:
    return HttpResponseForbidden("You are not allowed to edit this post.")

  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      form.instance.author = request.user 
      form.save()
      return redirect('post_detail', pk = post.pk)
    
  return render(request, 'blog/post_form.html', {'form': form})
#######


#### Delete post 

def delete_post(request, pk):
  post = Post.objects.get(id = pk)

  if request.user != post.author:
    return HttpResponseForbidden('You are not allow to delete this post')

  if request.method == 'POST':
    post.delete()
    return redirect('posts')  
  
  return render(request, 'blog/post_delete.html', {'post': post})


    


