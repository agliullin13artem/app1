from django.contrib.auth.decorators import login_required
from audioop import reverse
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

# для входа в профиль проверка
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт')

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse_lazy('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


# регистрация пользователя 
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, Вы успешно зарегистрировались и вошли в аккаунт')
            return HttpResponseRedirect(reverse_lazy('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


# профиль пользователя что бы отображдалисьего старые данные и изменять их
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Профайл успешно обновлен" )
            return HttpResponseRedirect(reverse_lazy('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users-cart.html')







@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Вы вышли из аккаунта')
    auth.logout(request)
    return redirect(reverse_lazy('main:index'))





