from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Homeviews.as_view(), name='home'),
    path('add-product', Addproduct.as_view(), name='add_product'),
    path('product/<int:pk>', views.Product_detail, name='product-detail'),
    path('/product/<int:pk>/update', Update_product.as_view(), name='update'),
    path('/product/<int:pk>/delete', Delete_product.as_view(), name='delete')

]