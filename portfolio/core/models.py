from django.db import models
from PIL import Image


class Intro(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    about = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description}"


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    picture = models.ImageField(upload_to="project_pics")
    content = models.TextField()

    def save(self):
        super().save()
        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    def __str__(self):
        return self.name
