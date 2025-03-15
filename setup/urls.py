from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('impressoras/', include('impressoras.urls')),
    path('', include('home.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('manutencoes/', include('manutencoes.urls')),
    path('telefones/', include('telefones.urls')),
]
