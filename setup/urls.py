from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.portfolio.urls')),
    path('', include('apps.projetos.urls')),
    path('', include('apps.jogos.urls')),
]
