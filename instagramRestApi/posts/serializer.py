from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')

class PostSerializer(serializers.ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'currentName', 'avatarUrl', 'caption', 'likes', 'createdAt', 'imageType', 'imageBinary', 'author']