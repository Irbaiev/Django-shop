from attr import field
from django.forms import ModelForm
from .models import Blog, Post_comment

class CommentForm(ModelForm):
    class Meta:
        model = Post_comment
        fields =('theme', 'comment',)


class add_post(ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'tags', 'image')
        
