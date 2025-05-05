from django.urls import path
from . import views

urlpatterns = [
    path('cftv/', views.cftv, name='cftv'),
    path('cad_cftv/', views.cad_cftv, name='cad_cftv'),
    path('dpto_cftv/', views.dpto_cftv, name='dpto_cftv'),
]