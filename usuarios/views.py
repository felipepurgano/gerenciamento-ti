from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

  
def register(request):
    if request.method == 'GET':
        return render(request, 'usuarios/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not password == confirm_password:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return render(request, 'usuarios/register.html')
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.WARNING, 'Usuário já existe.')
            return redirect('register')
        
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return redirect('/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do servidor.')
            return render(request, 'usuarios/register.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Usuário logado com sucesso!')
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválido!')
            return redirect('/')
        
def logout(request):
    auth.logout(request)
    return redirect('/')