from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict = {
        "title": "Home - главная",
        "content": "Магазин мебели HOME",
    }

    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    context: dict = {
        "title": "Home - о нас",
        "content": "О нас",
        "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар",
    }

    return render(request, "main/about.html", context)
