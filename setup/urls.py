from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('impressoras/', include('impressoras.urls')),
    path('', include('usuarios.urls')),
    path('manutencoes/', include('manutencoes.urls')),
    path('telefones/', include('telefones.urls')),
    path('cftv/', include('cftv.urls')),
    path('servidores/', include('servidores.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('emails/', include('emails.urls')),
]
