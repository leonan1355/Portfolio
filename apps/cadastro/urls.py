from django.urls import path
from apps.cadastro.views import cadastro, login, logout, conhecimento

urlpatterns = [
    path('projetos/cadastro', cadastro, name='projetos/cadastro'),
    path('projetos/login', login, name='projetos/login'),
    path('projetos/logout', logout, name='projetos/logout'),
    path('projetos/conhecimento', conhecimento, name='projetos/conhecimento'),
]