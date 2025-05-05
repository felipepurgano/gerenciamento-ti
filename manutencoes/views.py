from django.shortcuts import render, redirect

def manutencoes(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'manutencoes/manutencoes.html')
    
def dpto_manutencoes(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'manutencoes/dpto_manutencoes.html')