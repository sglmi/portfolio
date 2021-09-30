from django.db import models


class Intro(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    about = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description}"
