from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from pkg_resources import require
User = get_user_model()


class Blog(models.Model):

    tags_choice = (
        ('all', 'all'), ('technology', 'Technology'), ('food', 'Food'), ('fashion', 'Fashion')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=150, null=False)
    content = models.TextField(null=False)
    tags = models.CharField(default='all', choices=tags_choice, max_length=20)
    published = models.DateTimeField(null = True, default=timezone.now)
    image = models.ImageField(null=True, blank = True, upload_to='./image/blog')


    def __str__(self) -> str:
        return self.title



class Post_comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=100, null=False) 
    comment = models.TextField(null=False)


    def __str__(self) -> str:
        return self.theme
