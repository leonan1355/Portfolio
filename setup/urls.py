from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.portfolio.urls')),
    path('', include('apps.calculadora.urls')),
    path('', include('apps.jogo_da_velha.urls')),
]
