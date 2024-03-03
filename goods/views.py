from django.shortcuts import render

from goods.models import Products


# каталог
def catalog(request):
    goods = Products.objects.all()

    context={
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request,"goods/catalog.html", context)


# ссылка на продукты url по слагу
def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, "goods/product.html", context=context)
