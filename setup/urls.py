from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.portfolio.urls')),
    path('', include('apps.calculadora.urls')),
    path('', include('apps.jogo_da_velha.urls')),
    path('', include('apps.cadastro.urls')),
    path('', include('apps.numero_secreto.urls')),
    path('', include('apps.jogo_da_cobra.urls')),
    path('', include('apps.chatbox.urls')),
]
