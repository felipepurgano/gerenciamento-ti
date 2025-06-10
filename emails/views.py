from django.shortcuts import render, redirect

# Create your views here.
def emails(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'emails/emails.html')
    
def cadastrar_email(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'emails/cadastrar_email.html')
    elif request.method == 'POST':
        # Here you would handle the form submission and save the email
        # For now, just redirecting to the emails page
        return redirect('emails')
    
def listar_emails(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        # Here you would fetch the list of emails from the database
        # For now, just rendering an empty list
        return render(request, 'emails/listar_emails.html', {'emails': []})