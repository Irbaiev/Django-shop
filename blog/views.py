from re import template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . models import *
from . forms import *


class Bloglist(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'


def Blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    comment = Post_comment.objects.filter(post=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = blog
            form.save()
    else:
        form = CommentForm()


    return render(request, 'blog-detail.html', {'blog':blog, 'comment':comment, 'form':form})