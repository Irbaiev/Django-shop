from dataclasses import fields
from django.forms import ModelForm
from .models import Grade

class CommentForm(ModelForm):
    class Meta:
        model = Grade
        fields =('subject', 'rating', 'comment',)