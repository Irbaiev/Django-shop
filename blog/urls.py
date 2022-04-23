from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Bloglist.as_view(), name='blog'),
    path('post/<int:pk>', views.Blog_detail, name='blog-detail'),
    path('add-post', Addpost.as_view(), name='add-post')

]