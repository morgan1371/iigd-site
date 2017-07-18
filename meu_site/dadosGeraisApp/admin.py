from django.contrib import admin
from django.http import HttpResponse
from congressoPais_app.models import Participante,Crianca,Pesquisa

def participante_export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Participantes.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    
    writer.writerow([
        smart_str(u"model"),
        smart_str(u"ID"),
        smart_str(u"Usuario"),
        smart_str(u"Nome"),
        smart_str(u"Sobrenome"),
        smart_str(u"Profissão"),
        smart_str(u"Telefone"),
        smart_str(u"Celular"),
        smart_str(u"Data de nascimento"),
        smart_str(u"Vai participar"),
        ])
    for obj in queryset:
        writer.writerow([
            smart_str('Participante'),
            smart_str(obj.pk),
            smart_str(obj.usuario.email),
            smart_str(obj.nome),
            smart_str(obj.sobrenome),
            smart_str(obj.profissao),
            smart_str(obj.telefone),
            smart_str(obj.celular),
            smart_str(obj.data_nasc),
            smart_str(obj.vai_participar),
        ])
    
    return response
participante_export_csv.short_description = u"Exportar Participante CSV"

def crianca_export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Criancas.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"model"),
        smart_str(u"ID"),
        smart_str(u"Usuario"),
        smart_str(u"Nome"),
        smart_str(u"Sobrenome"),
        smart_str(u"Data de nascimento"),
        smart_str(u"Vai participar"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str('Crianca'),
            smart_str(obj.pk),
            smart_str(obj.usuario.email),
            smart_str(obj.nome),
            smart_str(obj.sobrenome),
            smart_str(obj.data_nasc),
            smart_str(obj.vai_participar),
        ])
    return response
crianca_export_csv.short_description = u"Exportar Criança CSV"

def pesquisa_export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Pesquisa.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"model"),
        smart_str(u"ID"),
        smart_str(u"Usuario"),
        smart_str(u"Pergunta"),
        smart_str(u"Resposta"),
    ])
    for obj in queryset:    
        writer.writerow([
            smart_str('Pesquisa'),
            smart_str(obj.pk),
            smart_str(obj.usuario.email),
            smart_str(obj.conhecimento),
            smart_str(obj.descreva),
        ])
    return response
pesquisa_export_csv.short_description = u"Exportar Pesquisa CSV"


def usuario_export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Usuários.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"model"),
        smart_str(u"email"),
        smart_str(u"Nome"),
        smart_str(u"Sobrenome"),
        smart_str(u"Logradouro"),
        smart_str(u"Complemento"),
        smart_str(u"Bairro"),
        smart_str(u"Cidade"),
        smart_str(u"Cep"),
        smart_str(u"CongressoPais"),
        smart_str(u"Data Criancao"),

    ])
    for obj in queryset:    
        writer.writerow([
            smart_str('Usuario'),
            smart_str(obj.email),
            smart_str(obj.nome),
            smart_str(obj.sobrenome),
            smart_str(obj.numero_endereco),
            smart_str(obj.complemento),
            smart_str(obj.bairro),
            smart_str(obj.cidade),
            smart_str(obj.cep),
            smart_str(obj.congressoPais),
            smart_str(obj.date_joined),
        ])
    return response
usuario_export_csv.short_description = u"Exportar Usuários CSV"

# Register your models here.
class ParticipanteModelAdmin(admin.ModelAdmin):
    list_filter=('usuario',)
    actions=[participante_export_csv]

# Register your models here.
class CriancaModelAdmin(admin.ModelAdmin):
    list_filter=('usuario',)
    actions=[crianca_export_csv]

class PesquisaModelAdmin(admin.ModelAdmin):
    list_filter=('usuario',)
    actions=[pesquisa_export_csv]

class UsuarioModelAdmin(admin.ModelAdmin):
    list_filter=('email',)
    actions=[usuario_export_csv]