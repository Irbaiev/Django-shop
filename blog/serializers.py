from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User

class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class Postserializers(serializers.ModelSerializer):
    user = Authorserializer(many=False, read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'content']
