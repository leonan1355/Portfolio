from django import forms

class LoginForms(forms.Form):
    email_login = forms.EmailField(
        label='Email:',
        required=True,
        max_length=60,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Digite seu email',
            }
        )
    )
    senha = forms.CharField(
        label='Senha:',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Digite sua senha',
            }
        )
    )
    
class CadastroForms(forms.Form):
    email_cadastro = forms.EmailField(
        label='Email para Cadastro:',
        required=True,
        max_length=60,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Digite seu email',
            }
        )
    )
    
    senha1 = forms.CharField(
        label='Senha para Cadastro:',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Digite sua senha',
            }
        )
    )
    
    senha2 = forms.CharField(
        label='Confirme sua Senha:',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Digite sua senha novamente',
            }
        )
    )