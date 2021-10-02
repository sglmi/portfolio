from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
