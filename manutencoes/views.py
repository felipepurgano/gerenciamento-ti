from django.shortcuts import render

def manutencoes(request):
    if request.method == 'GET':
        return render(request, 'manutencoes.html')