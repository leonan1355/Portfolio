from django.urls import path
from apps.jogo_da_cobra.views import jogo_da_cobra

urlpatterns = [
    path('jogos/jogo_da_cobra', jogo_da_cobra, name='jogos/jogo_da_cobra'),
]