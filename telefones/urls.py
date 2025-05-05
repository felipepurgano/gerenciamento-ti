from django.urls import path
from . import views

urlpatterns = [
    path('telefones/', views.telefones, name='telefones'),
    path('cad_telefone/', views.cad_telefone, name='cad_telefone'),
    path('dpto_tel/', views.dpto_tel, name='dpto_tel'),
]