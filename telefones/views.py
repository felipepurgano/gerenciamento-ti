from django.shortcuts import render

def telefones(request):
    if request.method == 'GET':
        return render(request, 'telefones/telefones.html')