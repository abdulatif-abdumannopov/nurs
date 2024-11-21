from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import FormView
from app.forms import *


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'contact-us.html', {'form':form})

def service(request):
    return render(request, 'service.html')

def account(request):
    return render(request, 'my-account.html')

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('account')  # Перенаправление после успешного входа
            else:
                form.add_error(None, 'Неверный логин или пароль')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически залогинить пользователя после регистрации
            return redirect('account')  # Перенаправление на главную страницу или страницу профиля
    else:
        form = RegistrationForm()

    return render(request, 'registration/create.html', {'form': form})

def custom_logout(request):
    logout(request)  # Завершаем сессию пользователя
    return redirect('login')