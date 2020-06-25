from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField

from ghostpost.models import Post

# https://stackoverflow.com/questions/28945327/django-rest-framework-with-choicefield
class PostSerializer(ModelSerializer):
    post_type = serializers.CharField(source='get_post_type_display')
    class Meta:
        model = Post
        fields = (
            'id',
            'post_type',
            'content',
            'up_vote',
            'down_vote',
            'sub_time',
            'hidden_key'
        )