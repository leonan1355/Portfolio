from django.urls import path
from apps.tftbuilder.views import tftbuilder

urlpatterns = [
    path('projetos/tftbuilder', tftbuilder, name='projetos/tftbuilder'),
]