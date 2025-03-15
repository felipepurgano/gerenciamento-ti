from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('impressoras/', views.impressoras, name='impressoras'),
    path('departamentos/', views.departamentos, name='departamentos'),
]
