from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.portfolio.urls')),
    path('', include('apps.calculadora.urls')),
    path('', include('apps.jogo_da_velha.urls')),
    path('', include('apps.cadastro.urls')),
    path('', include('apps.numero_secreto.urls')),
    path('', include('apps.jogo_da_cobra.urls')),
    path('', include('apps.tftbuilder.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
