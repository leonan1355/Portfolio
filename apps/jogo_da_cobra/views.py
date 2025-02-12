from django.shortcuts import render

def jogo_da_cobra(request):
    return render(request, 'jogos/jogo_da_cobra.html')

