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
    queryset = Post.objects.all().order_by('-sub_time')

    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        post.up_vote += 1
        post.save()
        print(post.up_vote)
        return Response(post.up_vote)

    @action(detail=True, methods=['post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        post.down_vote += 1
        post.save()
        return Response("Down Voted")

    @action(detail=False)
    def boasts(self, request):
        boast_posts = Post.objects.filter(post_type='b')
        serializer = self.get_serializer(boast_posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roast_posts = Post.objects.filter(post_type='r')
        serializer = self.get_serializer(roast_posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest_rated(self, request):
        all_posts = Post.objects.all()
        for post in all_posts:
            score = post.vote_score
            post.score = score
            post.save()
        rated_posts = all_posts.order_by('-score')
        serializer = self.get_serializer(rated_posts, many=True)
        return Response(serializer.data)