from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    boast = 'b'
    roast = 'r'
    post_choices = {
        (boast, 'Boast'),
        (roast, 'Roast'),
    }

    post_type = models.CharField(
        max_length=10,
        choices=post_choices,
        default=boast,
    )

    content = models.CharField(max_length=280)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    sub_time = models.DateTimeField(default=timezone.now)
    hidden_key = models.CharField(max_length=6, blank=True)
    
    # https://www.youtube.com/watch?v=jCzT9XFZ5bw
    @property
    def vote_score(self):
        return self.up_vote - self.down_vote

    def __str__(self):
        return self.content