from django.urls import path
from . import views

urlpatterns = [
    path('servidores/', views.servidores, name='servidores'),
]
