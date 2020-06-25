from django.forms import modelform_factory
from ghostpost.models import Post

AddPostForm = modelform_factory(Post, exclude=['up_vote', 'down_vote', 'sub_time', 'score'])