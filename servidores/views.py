from django.shortcuts import render

def servidores(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'servidores/servidores.html')