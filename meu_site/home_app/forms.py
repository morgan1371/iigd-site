from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Um formulário que cria um usuário, sem privilégios, através de
    seu email e senha e outros campos
    """
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.exclude = ('username',)
        for key in self.fields:
            self.fields[key].required = True
    class Meta:
        model = CustomUser
        fields = (
            'nome','sobrenome',
            'logradouro','numero_endereco','complemento',
            'bairro','cidade','cep',
            'email',
        )

class CustomUserChangeForm(UserChangeForm):
    """
    Um formulário que cria um usuário, sem privilégios, através de
    seu email e senha e outros campos
    """
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.exclude = ('username',)
    
    class Meta:
        model = CustomUser
        fields = (
            'nome','sobrenome',
            'logradouro','numero_endereco','complemento',
            'bairro','cidade','cep',
            'email',
        )