from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Обробка реєстрації користувача
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Обробка входу користувача
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
