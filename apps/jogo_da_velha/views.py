from django.shortcuts import render

def jogo_da_velha(request):
    return render(request, 'jogos/jogo_da_velha.html')
