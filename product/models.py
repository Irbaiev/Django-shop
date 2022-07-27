from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()



class Product(models.Model):
    title = models.CharField(unique=True, max_length=50, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, null=False)
    rating = models.IntegerField(default=1, choices=Choice_raiting, max_length=12)
    comment = models.TextField(null=False)
    created = models.DateTimeField(null = True, default=timezone.now)

    def __str__(self) -> str:
        return f'Комментарий {self.subject}Продукт{ self.products}'
        
