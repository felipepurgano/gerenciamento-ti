from django.shortcuts import render, redirect

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'dashboard/dashboard.html')