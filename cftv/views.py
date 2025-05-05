from django.shortcuts import render

def cftv(request):
    if request.method == 'GET':
        return render(request, 'cftv/cftv.html')
    
def cad_cftv(request):
    if request.method == 'GET':
        return render(request, 'cftv/cad_cftv.html')

def dpto_cftv(request):
    if request.method == 'GET':
        return render(request, 'cftv/dpto_cftv.html')