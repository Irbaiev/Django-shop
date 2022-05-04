from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Blog_list, name='blog'),
    path('post/<int:pk>', views.Blog_detail, name='blog-detail'),
    path('post/<int:pk>/delete', Deletepost.as_view(), name='delete_post'),
    path('add-post', Addpost.as_view(), name='add-post'),
    path('post/<int:pk>/edit-post', Editpost.as_view(), name='edit-post'),

]