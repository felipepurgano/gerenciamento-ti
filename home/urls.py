from django.urls import path
from . import views

urlpatterns = [
    path('categorias', views.categorias, name='categorias'),
    path('', views.home, name='home'),
]
