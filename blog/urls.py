from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Blog_views.as_view(), name='blog'),
    path('post/<int:pk>', views.Blog_detail, name='blog-detail'),
    path('post/<int:pk>/delete', Deletepost.as_view(), name='delete_post'),
    path('add-post', post.as_view(), name='add-post'),
    path('post/<int:pk>/edit-post', Editpost.as_view(), name='edit-post'),
    path('api/v1/posts', BloglistApi.as_view(), name = 'blogapi'),
    path('api/v1/posts/<int:pk>', BlogDetailApi.as_view(), name = 'blogdetailapi'),
    path('api/v1/create', CreatePostAPI.as_view(), name='createviews')


]