from django.shortcuts import render
import os
from together import Together

api_key = str(os.getenv('TOGETHER_API_KEY'))

client = Together(api_key=api_key)

def perguntar(mensagem, contexto):
    resposta = client.chat.completions.create(
         model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
         messages=contexto
    )
    return resposta.choices[0].message.content


def chatbox(request):
    tela1 = ''
    tela2 = ''

    if request.method=='POST':
        tela1 = request.POST.get('tela1', '').strip()
        tela2 = request.POST.get('tela2', '').strip()
        if tela2:
            contexto = [{"role":"user", "content": msg} for msg in tela1.split("\n\nVocê: ") if msg.strip()]
            contexto.append({"role":"user", "content": tela2})

            resposta = perguntar(tela2, contexto)
            tela1 += f"\n\nVocê: {tela2}\n\nBot: {resposta}\n"
            tela2 = ''
            
    return render(request, 'projetos/chatbox.html', {'tela1': tela1, 'tela2': tela2})