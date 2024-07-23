from django.urls import path
from apps.projetos.views import projetos

urlpatterns = [
    path('projetos/', projetos, name='projetos')
]