from django.urls import path
from apps.jogos.views import jogos

urlpatterns = [
    path('jogos/', jogos, name='jogos')
]