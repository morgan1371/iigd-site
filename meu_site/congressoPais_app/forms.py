from django import forms
from .models import Participante, Crianca, Pesquisa
from django.utils.translation import ugettext_lazy as _
from meu_site import settings
from datetime import date
from datetimewidget.widgets import DateWidget



class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        exclude = ('usuario',)

class CriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        exclude = ('usuario',)

class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        exclude = ('usuario',)