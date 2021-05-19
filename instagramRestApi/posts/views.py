from rest_framework import viewsets
from .models import User, Post
from .serializer import UserSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-createdAt')
    serializer_class = PostSerializer
    filter_fields = ('author',)