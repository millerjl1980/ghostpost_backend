from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer
from ghostpost.models import Post

# Create your views here.
class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'posts'
    queryset = Post.objects.all()