from django.urls import path
from . import views

urlpatterns = [
    path('cftv/', views.cftv, name='cftv'),
]