from django.shortcuts import render

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
def impressoras(request):
    if request.method == 'GET':
        return render(request, 'impressoras.html')

def departamentos(request):    
    if request.method == 'GET':
        return render(request, 'departamentos.html')