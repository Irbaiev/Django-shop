from tkinter import image_names, image_types
from django.test import TestCase

from .models import Product, Grade
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
from django.core.files import File

class test_product(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username = 'Adam',
            email = 'Adam_irbaiev@gmail.com',
            password = 'secretpassword',
            
        )


        self.product = Product.objects.create(
            title = 'Test product',
            price = '125',
            category = 'new category',
            availibility = 'In stock',
            description = 'description',
            image = File(open('./ppp.png', 'rb'))
        )

        self.grade = Grade.objects.create(
            products = self.product,
            author = self.user,
            subject = 'Good product',
            rating = '1',
            comment = 'The good shop'
        )


    def test_product(self):
        self.assertEqual(f'{self.product.title}', 'Test product')
        self.assertEqual(f'{self.product.price}', '125')
        self.assertEqual(f'{self.product.category}', 'new category')
        self.assertEqual(f'{self.product.availibility}', 'In stock')
        self.assertEqual(f'{self.product.description}', 'description')
        self.assertEqual(f'{self.product.image}', 'image/ppp.png')

    def test_product_comm(self):
        self.assertEqual(f'{self.grade.products}', 'Test product')
        self.assertEqual(f'{self.grade.author}', 'Adam')
        self.assertEqual(f'{self.grade.subject}', 'Good product')
        self.assertEqual(f'{self.grade.rating}', '1')
        self.assertEqual(f'{self.grade.comment}', 'The good shop')

    def test_views(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

