from django.urls import path
from . import views

urlpatterns = [
    path('cad_impressora/', views.cad_impressora, name='cad_impressora'),
    path('impressoras/', views.impressoras, name='impressoras'),
    path('departamentos/', views.departamentos, name='departamentos'),
    path('listar_equipamentos/', views.lista_impressoras, name='listar_equipamentos'),
    path('manutencoes/', views.listar_manutencoes, name='listar_manutencoes'),
    path('manutencoes/adicionar/', views.manutencoes_imp, name='manutencoes_imp'),
    path('departamentos/adicionar/', views.cadastrar_departamento, name='cadastrar_departamento'),
    path('troca_toner/', views.troca_toner, name='troca_toner'),
]