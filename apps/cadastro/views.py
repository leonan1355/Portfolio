from django.shortcuts import render, redirect
from apps.cadastro.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator

account_activation_token = PasswordResetTokenGenerator()

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
                is_active=False,
            )
            usuario.save()
            subject = 'Confirme seu cadastro'
            uid = urlsafe_base64_encode(force_bytes(usuario.pk))
            token = account_activation_token.make_token(usuario)
            link = request.build_absolute_uri(f'/projetos/confirmar_email/{uid}/{token}/')
            message = render_to_string('projetos/email_confirmacao.html', {
                'user': usuario,
                'link': link,
            })
            send_mail(subject, message, 'leonan.ferreira.dev@gmail.com', [email])
            
            messages.success(request, 'Cadastro iniciado! Por favor, confirme seu email.')
            return redirect('projetos/login')
    return render(request, 'projetos/cadastro.html', {'form': form})

def confirmar_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        usuario = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        usuario = None
    if usuario is not None and account_activation_token.check_token(usuario, token):
        usuario.is_active = True
        usuario.save()
        messages.success(request, 'Email confirmado com sucesso!')
        return redirect('projetos/login')
    else:
        messages.error(request, 'Link inválido ou expirado!')
        return redirect('projetos/cadastro')
    
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
