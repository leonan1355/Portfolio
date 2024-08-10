from django.shortcuts import render
import re

def removedor_de_zeros(num):
    """Remove zeros a esquerda de um número, mantendo pelo menos um dígito"""
    return num.lstrip('0') or '0'

def processar_expressao(calculo):
    """Remover zeros a esquerda de todos os números da expressão"""
    partes = re.split(r'([+\-*/])', calculo)
    resultado = []
    for parte in partes:
        if parte and parte[0].isdigit():
            parte_sem_zeros = removedor_de_zeros(parte)
            if len(parte_sem_zeros)>9:
                resultado.append(parte_sem_zeros[:9])
            else:
                resultado.append(parte_sem_zeros)
        else:
            resultado.append(parte)
    return ''.join(resultado)

def calcular(expressao):
    """Calcula a expressão fornecida e retorna o resultado formatado"""
    try:
        resultado = f"{eval(expressao):.6f}".rstrip('0').rstrip('.')
    except:
        resultado = '0'
    return resultado

def calculadora(request):
    operadores = '-+/*'
    tela1 = ''
    tela2 = ''
    
    if request.method=='POST':
        tela1 = request.POST.get('tela1', '')
        tela2 = request.POST.get('tela2', '')
        botao = request.POST.get('botao')
        if botao == 'c' or botao=='off':
            tela1 = ''
            tela2 = ''
        elif botao == 'on':
            tela2 = 'Bem-vindo!'
        elif botao == '=':
            if tela2 and tela1:
                tela1 += tela2
                tela1 = processar_expressao(tela1)
                tela2 = calcular(tela1)
                tela1 = ''
            else:
                tela2 = '0'
        elif botao in operadores:
            if tela2:
                if tela1:
                    tela1 += tela2
                    tela1 = processar_expressao(tela1)
                    tela2 = calcular(tela1)
                    tela1 = tela2 + botao
                    tela2 = ''
                else:
                    tela1 = processar_expressao(tela2) + botao
                    tela2 = ''
            elif tela1 and tela1[:-1] in operadores:
                tela1 = tela1[:-1] + botao
        else:
            if tela2 == 'Bem-vindo!':
                tela2 = botao
            else:
                tela2 = processar_expressao(tela2 + botao)
    else:
        tela2=''
    return render(request, 'projetos/calculadora.html', {'tela1': tela1, 'tela2': tela2})