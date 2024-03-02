from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()


    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)


def about(request):
    content = {
        'title': 'HOME - о нас',
        'content': 'О нас',
        'text_on_page': 'О том почему этот маганзин такой классный и какие в нем хорошие товары'
    }

    return render(request, 'main/about.html', content )