from django.urls import path
from apps.calculadora.views import calculadora

urlpatterns = [
    path('projetos/calculadora', calculadora, name='projetos/calculadora'),
]