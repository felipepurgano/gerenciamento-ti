from django.shortcuts import render, redirect

def telefones(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'telefones/telefones.html')
    
def cad_telefone(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'telefones/cad_tel.html')

def dpto_tel(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'telefones/dpto_tel.html')
    
def listar_tel(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'telefones/listar_tel.html')