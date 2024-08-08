from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories



class IndexView(TemplateView):
    template_name ='main/index.html'


    def get_context_date(self, **kwargs):
        context = super().get_context_date(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = 'Магазин мебели HOME'
        return context
        
# def index(request):
#     context = {
#         'title': 'Home - Главная',
#         'content': 'Магазин мебели HOME',
#     }

#     return render(request, 'main/index.html', context)


class AboutView(TemplateView):
    template_name ='main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'О том почему этот маганзин такой классный и какие в нем хорошие товары'
        return context

# def about(request):
#     content = {
#         'title': 'HOME - о нас',
#         'content': 'О нас',
#         'text_on_page': 'О том почему этот маганзин такой классный и какие в нем хорошие товары'
#     }

#     return render(request, 'main/about.html', content )