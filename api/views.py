from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import PostSerializer
from ghostpost.models import Post

# Create your views here.
class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'posts'
    queryset = Post.objects.all()

    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        post.up_vote += 1
        post.save()
        return Response("Up Voted")

    @action(detail=True, methods=['post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        post.down_vote += 1
        post.save()
        return Response("Down Voted")

    # @action(detail=False)
    # def boasts(self, request):
    #     pass

    # @action(detail=False)
    # def roasts(self, request):
    #     pass

    # @action(detail=False)
    # def highest_rated(self, request):
    #     pass