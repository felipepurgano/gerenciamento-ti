from django.shortcuts import render

def cftv(request):
    if request.method == 'GET':
        return render(request, 'cftv/cftv.html')