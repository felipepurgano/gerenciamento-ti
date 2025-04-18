from django.shortcuts import render

def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    
def register(request):
    if request.method == 'GET':
        return render(request, 'usuarios/register.html')