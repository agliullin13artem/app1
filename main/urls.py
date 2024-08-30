
from django.urls import path

from main.views import AboutView, IndexView
from django.views.decorators.cache import cache_page


app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', cache_page(60)(AboutView.as_view()), name='about')

]
