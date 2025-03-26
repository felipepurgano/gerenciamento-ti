from django.urls import path
from . import views

urlpatterns = [
    path('cad_impressora/', views.cad_impressora, name='cad_impressora'),
    path('impressoras/', views.impressoras, name='impressoras'),
    path('departamentos/', views.departamentos, name='departamentos'),
]
