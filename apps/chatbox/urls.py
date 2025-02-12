from django.urls import path
from apps.chatbox.views import chatbox

urlpatterns = [
    path('projetos/chatbox', chatbox, name='projetos/chatbox'),
]