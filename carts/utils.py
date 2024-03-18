from carts.models import Cart


# утилиты по каждому юзеру возращает карзыны кверисет
def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)