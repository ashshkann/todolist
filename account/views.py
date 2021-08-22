from django.shortcuts import render, redirect
from .forms import FormLogin, FormRegister
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

def viewForm(request):
    if request.user.is_authenticated:
        return redirect('/')

    form_login = FormLogin(request.POST or None)
    if form_login.is_valid():
        user_name = form_login.cleaned_data.get('user_name')
        password = form_login.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form_login.add_error('user_name', 'username or password is not corecct')

    context = {
        'form': form_login,
    }
    return render(request, 'login.html', context)

def viewregister(request):
    if request.user.is_authenticated:
        return redirect('/')
    form_register = FormRegister(request.POST or None)
    if form_register.is_valid():
        user_name = form_register.cleaned_data.get("user_name")
        email = form_register.cleaned_data.get("email")
        password = form_register.cleaned_data.get("password")
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/login')  
    context={
        'form': form_register
    }
    return render(request, 'register.html', context)

def viewlogout(request):
    logout(request)
    return redirect('/login')