from django.urls import path
from . import views

urlpatterns = [
    path('manutencoes/', views.manutencoes, name='manutencoes'),
    path('dpto_manutencoes/', views.dpto_manutencoes, name='dpto_manutencoes'),
]