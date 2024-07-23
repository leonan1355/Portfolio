from django.urls import path
from apps.portfolio.views import home, habilidades, sobre_mim, download_cv

urlpatterns = [
    path('', home, name='home'),
    path('download_cv/', download_cv, name='download_cv'),
    path('habilidades/', habilidades, name='habilidades'),
    path('sobre_mim', sobre_mim, name='sobre_mim'),
]