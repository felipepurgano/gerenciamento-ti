from django.urls import path
from . import views

urlpatterns = [
    path('cftv/', views.cftv, name='cftv'),
    path('cad_cftv/', views.cad_cftv, name='cad_cftv'),
]