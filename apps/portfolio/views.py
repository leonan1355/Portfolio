from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from datetime import datetime

def home(request):
    return render(request, 'portfolio/home.html')

def download_cv():
    """Função que possibilita o download do cv"""
    return HttpResponseRedirect(settings.STATIC_URL + 'assets/files/cv_leonan.docx')

def calcular_idade(data_nascimento):
    """Função que calcula minha idade para evitar atualizações anuais"""
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade

def sobre_mim(request):
    data_nascimento = '1998-05-05'
    idade = calcular_idade(data_nascimento)
    return render(request, 'portfolio/sobre_mim.html', {'idade': idade})

def habilidades(request):
    return render(request, 'portfolio/habilidades.html')

def projetos(request):
    return render(request, 'portfolio/projetos.html')

def jogos(request):
    return render(request, 'portfolio/jogos.html')
