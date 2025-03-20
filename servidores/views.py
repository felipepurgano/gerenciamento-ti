from django.shortcuts import render

def servidores(request):
    if request.method == 'GET':
        return render(request, 'servidores/servidores.html')