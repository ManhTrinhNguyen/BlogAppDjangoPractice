from django.urls import path
from . import views 
urlpatterns = [
  path('', views.PostListView.as_view(), name = 'posts'),
  path('post/<int:pk>/', views.PostDetail.as_view(), name = 'post_detail'),
  path('post/new/', views.PostCreateView.as_view(), name = 'post_form'),
  path('post/update/<int:pk>', views.update_post, name = 'post_update'),
  path('post/delete/<int:pk>', views.delete_post, name = 'post_delete')
]