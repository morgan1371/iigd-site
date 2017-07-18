from django.contrib import admin
from .models import Participante,Crianca,Pesquisa
from dadosGeraisApp.admin import ParticipanteModelAdmin,CriancaModelAdmin,PesquisaModelAdmin
# Register your models here.
admin.site.register(Participante, ParticipanteModelAdmin)
admin.site.register(Crianca, CriancaModelAdmin)
admin.site.register(Pesquisa, PesquisaModelAdmin)