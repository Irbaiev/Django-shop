from xml.etree.ElementTree import Comment
from django.test import TestCase


from .models import Blog, Post_comment
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse

class Blogtest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username = 'Adam',
            email = 'Adam_irbaiev@gmail.com',
            password = 'secretpassword',
            
        )

        self.blog = Blog.objects.create(
            user = self.user,
            title = 'Test',
            content = 'This is test content',
            tags = 'all',
        ) 

        self.comment = Post_comment.objects.create(
            post = self.blog,
            user = self.user,
            theme = 'Good post',
            comment = 'The good blog',
        )

    def test_blog(self):
        self.assertEqual(f'{self.blog.title}', 'Test')   
        self.assertEqual(f'{self.blog.user}', 'Adam')    
        self.assertEqual(f'{self.blog.content}', 'This is test content')    
        self.assertEqual(f'{self.blog.tags}', 'all') 


    def test_comment(self):
        self.assertEqual(f'{self.comment.post}', 'Test')
        self.assertEqual(f'{self.comment.user}', 'Adam')
        self.assertEqual(f'{self.comment.theme}', 'Good post')
        self.assertEqual(f'{self.comment.comment}', 'The good blog')


    def test_blog_views(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')