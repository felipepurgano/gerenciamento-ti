from django.urls import path
from . import views

urlpatterns = [
    path('emails/', views.emails, name='emails'),
    path('emails/cadastrar_email/', views.cadastrar_email, name='cadastrar_email'),
    path('emails/listar_emails/', views.listar_emails, name='listar_emails'),
]
