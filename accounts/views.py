from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # немесе 'home'
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Сіз сәтті кірдіңіз!")
            return redirect('home')
        else:
            messages.error(request, "Қате логин немесе пароль!")

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Сіз аккаунттан шықтыңыз!")
    return redirect('home')
