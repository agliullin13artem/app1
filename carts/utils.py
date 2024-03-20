from carts.models import Cart


# утилиты по каждому юзеру возращает карзыны кверисет
def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    

    # созадем ссессионый ключ для пользователя если он не авторизован
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key)