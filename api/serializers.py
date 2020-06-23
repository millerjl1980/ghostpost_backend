from rest_framework.serializers import ModelSerializer

from ghostpost.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'post_type',
            'content',
            'up_vote',
            'down_vote',
            'sub_time',
            'hidden_key'
        )