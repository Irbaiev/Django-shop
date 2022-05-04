from attr import field
from django.forms import ModelForm
from .models import Blog, Post_comment

class CommentForm(ModelForm):
    class Meta:
        model = Post_comment
        fields =('theme', 'comment',)


        
