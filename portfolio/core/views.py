from django.shortcuts import render

from . import models


def index(request):
    context = {
        "intro": models.Intro.objects.all(),
        "projects": models.Project.objects.all(),
    }
    return render(request, "core/index.html", context)
