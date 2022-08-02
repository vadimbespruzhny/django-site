from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, UserChangeForm, CustomUserChangeForm, PasswordChangeForm
from orders.models import Order, OrderItem
# Create your views here.


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('index')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def change_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'change_profile.html', {'form': form})


def password_change(request):
    if request.method == 'POST':
        # заполняем форму данными из запроса
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            # получаем старый пароль
            old_pass = form.cleaned_data['old_pwd']
            # получаем новый пароль из формы
            new_pass = form.cleaned_data['new_pwd2']
            # получаем имя пользователя
            username = request.user.username
            # аутентифицируем пользователя подставляя имя и старый пароль
            user = authenticate(username=username, password=old_pass)
            if user is not None:
                # устанавляваем новый пароль
                user.set_password(new_pass)
                # сохраняем пользователя с новым паролем
                user.save()
        return redirect('login')
    else:
        form = PasswordChangeForm()
        return render(request, 'password_change_form.html', {'form': form})






