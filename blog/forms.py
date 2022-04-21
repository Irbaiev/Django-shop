from django.forms import ModelForm
from .models import Post_comment

class CommentForm(ModelForm):
    class Meta:
        model = Post_comment
        fields =('theme', 'comment',)
