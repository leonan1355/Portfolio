from django.shortcuts import render

def tftbuilder(request):
    return render(request, 'projetos/tftbuilder.html')