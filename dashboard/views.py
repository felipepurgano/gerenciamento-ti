from django.shortcuts import render

def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard/dashboard.html')