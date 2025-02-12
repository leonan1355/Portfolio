from django.urls import path
from apps.numero_secreto.views import numero_secreto

urlpatterns = [
    path('jogos/numero_secreto', numero_secreto, name='jogos/numero_secreto'),
]