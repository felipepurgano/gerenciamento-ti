from django.shortcuts import render

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'impressoras/cadastro.html')
    
def impressoras(request):
    if request.method == 'GET':
        return render(request, 'impressoras/impressoras.html')

def departamentos(request):    
    if request.method == 'GET':
        return render(request, 'impressoras/departamentos.html')