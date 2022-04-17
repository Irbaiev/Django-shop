from datetime import timezone
from wsgiref.simple_server import demo_app
from django.db import models
from django.conf import settings
from django.utils import timezone



class Product(models.Model):
    title = models.CharField(unique=True, max_length=50, null=False)
    price = models.IntegerField(null=False, default=0)
    category = models.CharField(max_length=20, null=False, default='new category')
    availibility = models.CharField(max_length=20, default='In stock')
    description = models.CharField(max_length=500, null=False, default='description')
    image = models.ImageField(null=True, blank = True, upload_to='./image', verbose_name='image')

    def __str__(self) -> str:
        return self.title



class Grade(models.Model):
    Choice_raiting = (
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
        )


    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, null=False)
    rating = models.IntegerField(default=1, choices=Choice_raiting, max_length=12)
    comment = models.TextField(null=False)
    created = models.DateTimeField(null = True, default=timezone.now)

    def __str__(self) -> str:
        return f'Комментарий {self.subject}Продукт{ self.products}'
        
