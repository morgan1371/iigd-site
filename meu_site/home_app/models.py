from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils.http import urlquote
from django.core.validators import MinLengthValidator, MinValueValidator
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,is_staff,is_superuser,**extra_fields):
        """
        Cria e salva um Usuario com email e senha
        """
        now = timezone.now

        if not email:
            raise ValueError('O email precisa ser determinado!')
        
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        
        user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    #basico
    nome = models.CharField(_('Primeiro nome'), max_length=254, blank=True)
    sobrenome = models.CharField(_('Sobrenome'), max_length=254, blank=True)
    email = models.EmailField(_('E-mail'), blank=True, unique=True)

    #endereço
    logradouro = models.CharField(_('Logradouro'), max_length=254,blank=True)
    numero_endereco = models.IntegerField(_('Nº'),blank=True, validators=[MinValueValidator(1)])
    complemento = models.CharField(_('Complemento'), max_length=254,blank=True)
    bairro = models.CharField(_('Bairro'), max_length=150,blank=True)
    cidade = models.CharField(_('Cidade'), max_length=100,blank=True)
    cep = models.CharField(_('CEP'), max_length=8,blank=True,validators=[MinLengthValidator(8)],help_text='CEP 8 digitos (sem traços)')
    
    #eventos
    congressoPais = models.BooleanField(default=False)

    #configs
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
            'nome','sobrenome',
            'logradouro','numero_endereco','complemento',
            'bairro','cidade','cep',
    ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')

    def get_absolute_url(self):
        return "/usuarios/%s/" % urlquote(self.email)

    def get_short_name(self):
        """
        Retorna o primeiro nome
        """
        return self.nome.strip()

    def get_full_name(self):
        """
        Retorna o nome completo e espaçado
        """
        nome_completo = '%s %s' % (self.nome, self.sobrenome)
        return nome_completo.strip()
    
    def email_user(self, subject, message, from_email=None):
        """
        Envia um email para este usuario
        """
        send_mail(subject,message,[self.email])