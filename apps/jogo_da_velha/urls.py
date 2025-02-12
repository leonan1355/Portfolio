from django.urls import path
from apps.jogo_da_velha.views import jogo_da_velha

urlpatterns = [
    path('jogos/jogo_da_velha', jogo_da_velha, name='jogos/jogo_da_velha'),
]