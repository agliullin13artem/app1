from django.core.paginator import Paginator
from django.shortcuts import  get_list_or_404, render

from goods.models import Products


# каталог  все товары и тд 
def catalog(request, category_slug):

    page = request.GET.get('page', 1)





    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        
    paginator = Paginator(goods, 3) # пагинатор количество элементов на одной странице
    current_page = paginator.page(int(page))

    context={
        "title": "Home - Каталог",
        "goods": current_page,
        'slug_url': category_slug,
    }
    return render(request,"goods/catalog.html", context)


# ссылка на продукты url по слагу
def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, "goods/product.html", context=context)
