from django.shortcuts import render

def numero_secreto(request):
    return render(request, 'jogos/numero_secreto.html')