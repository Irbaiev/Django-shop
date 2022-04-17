from django.urls import path
from .views import *

urlpatterns = [

    path('registration/', Singup.as_view(), name='singup')
    
]