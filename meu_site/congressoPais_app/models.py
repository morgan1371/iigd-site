from django.db import models
from home_app.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone
import re
# Create your models here.
class Participante(models.Model):
    usuario = models.ForeignKey(CustomUser)
    nome = models.CharField(_('Primeiro nome'), max_length=254)
    sobrenome = models.CharField(_('Sobrenome'), max_length=254)
    profissao = models.CharField(_('Profissão'), max_length=254)
    telefone = models.CharField(_('Telefone'), max_length=10, help_text='Ex.: 7133990000 -> 10 digitos' ,
    validators=[
        MinLengthValidator(10),
    ])
    celular = models.CharField(_('Celular'), max_length=11, help_text='Ex.: 71998123456 -> 11 ou 10 (sem o 9 adicional) digitos' ,validators=[
        MinLengthValidator(10),
    ])
    data_nasc = models.DateField(_('Data de Nascimento'), default=timezone.now)

    vai_participar = models.BooleanField(verbose_name = _('Irá ao evento?'), default=False)

    REQUIRED_FIELDS = '__all__'

    def __str__(self):
        return "%s %s | %s" % (self.nome,self.sobrenome,self.usuario)

class Crianca(models.Model):
    usuario = models.ForeignKey(CustomUser)
    nome = models.CharField(_('Primeiro nome'), max_length=254)
    sobrenome = models.CharField(_('Sobrenome'), max_length=254)
    data_nasc = models.DateField(_('Data de Nascimento'), default=timezone.now)

    vai_participar = models.BooleanField(verbose_name = _('Irá ao evento?'), default=False)

    REQUIRED_FIELDS = '__all__'

    def __str__(self):
        return "%s %s | %s" % (self.nome,self.sobrenome,self.usuario)

class Pesquisa(models.Model):
    usuario = models.OneToOneField(CustomUser)
    CONHECIMENTO_CHOICES = [
        ('igreja','Qual igreja?'),
        ('perfil','Em qual perfil?'),
        ('pagina','Em qual página?')
    ]
    conhecimento = models.CharField(_('Como conheceu o congresso'),choices=CONHECIMENTO_CHOICES, max_length=6)
    descreva = models.CharField(_('Resposta'), max_length=254,blank=True)
    
    REQUIRED_FIELDS = '__all__'

    def __str__(self):
        return "Pesquisa de %s" % (self.usuario)
    