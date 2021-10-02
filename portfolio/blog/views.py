from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, "blog/index.html", {"posts": posts})
