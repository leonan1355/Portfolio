from django.shortcuts import render, redirect
from apps.cadastro.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            if form['senha1'].value() != form['senha2'].value():
                messages.error(request, 'Senhas não são iguais!')
                return redirect('projetos/cadastro')
            email = form['email_cadastro'].value()
            senha = form['senha1'].value()
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Este email já foi cadastrado!')
                return redirect('projetos/cadastro')
            usuario = User.objects.create_user(
                username=email,
                password=senha,
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado!')
            return redirect('projetos/login')
    return render(request, 'projetos/cadastro.html', {'form': form})

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            email = form['email_login'].value()
            senha = form['senha'].value()
        usuario = auth.authenticate(
            request,
            username=email,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Usuário logado!')
            return redirect('projetos/conhecimento')
        else:
            messages.error(request, 'Erro ao efetuar login!')
            return redirect('projetos/login')
    return render(request, 'projetos/login.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        messages.success(request, 'Usuário deslogado!')
        auth.logout(request)
    else:
        messages.error(request, 'Usuário não está logado!')
    return redirect('projetos/login')

def conhecimento(request):
    if not request.user.is_authenticated:
        messages.error(request, 'O conhecimento milenar só é acessível a usuários logados!')
        return redirect('projetos/login')
    return render(request, 'projetos/conhecimento.html')
