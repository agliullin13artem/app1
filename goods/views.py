from django.core.paginator import Paginator
from django.shortcuts import  get_list_or_404, render

from goods.models import Products


# каталог  все товары и тд 
def catalog(request, category_slug):

# пагинация и фильр товара на главной странице
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
# фильтр сортировки товара по убыванию и возрастанию и по скидке на главной странице
    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    
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
