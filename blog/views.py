from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.db.models import Q

from . models import *
from . forms import *


def Blog_list(request):
    search_query = request.GET.get('q')

    if search_query:
        blogs = Blog.objects.filter(Q(title__icontains=search_query) | Q(tags__icontains=search_query))
    else:
        blogs = Blog.objects.all()

    return render(request, 'blog.html', {'blogs':blogs})



def Blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    comment = Post_comment.objects.filter(post=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Комментарий добавлен')
            form = form.save(commit=False)
            form.user = request.user
            form.post = blog
            form.save()
    else:
        form = CommentForm()


    return render(request, 'blog-detail.html', {'blog':blog, 'comment':comment, 'form':form})



class Addpost(CreateView):
    model = Blog
    template_name = 'add-post.html'
    context_object_name = 'add_posts'
    fields = ('title', 'content', 'tags')
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)


class Deletepost(DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = '/blog'


class Editpost(UpdateView):
    model = Blog
    template_name = 'edit-post.html'
    fields = ('title', 'content', 'tags')
    success_url = 'post/<int:pk>'


# class Search_views(ListView):

#     def get_queryset(self):
#         return Blog.objects.filter(title__icontains=self.request.GET.get("q"))


#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['q'] = self.request.GET.get("q")
#         return context

    