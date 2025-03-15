from django.urls import path
from . import views

urlpatterns = [
    path('telefones/', views.telefones, name='telefones'),
]