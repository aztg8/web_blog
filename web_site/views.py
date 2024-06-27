from django.shortcuts import render

from .models import *


def index(request):
    categories = Category.objects.all()
    articles = Articles.objects.all()

    context = {
        "categories": categories,
        "articles": articles,
        "title": "Главная страница"
    }

    return render(request, 'index.html', context)
