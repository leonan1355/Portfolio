from django.shortcuts import render

def jogos(request):
    return render(request, 'jogos/jogos.html')
