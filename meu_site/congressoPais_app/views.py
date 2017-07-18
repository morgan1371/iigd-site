from django.shortcuts import render, redirect, reverse
from .forms import ParticipanteForm,CriancaForm,PesquisaForm
from .models import Participante, Crianca, Pesquisa
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Template, RequestContext
from collections import defaultdict
from home_app.models import CustomUser
# Create your views here.


def form_invalido(request, direcao, mensagem='Você preencheu algo de errado.'):
    """
    Aplica HttpResponseRedirect.
    """
    return HttpResponse(Template('{% extends "base.html" %}{% block content %}' +
           '''
                <h2>{}</h2>
                <p>Volte para o inicio, clique <a href={}>aqui.</a> </p>
           
           '''.format(mensagem, direcao) + '{% endblock %}'
        ).render(RequestContext(request)))


def index(request):
    args = {}
    args_fam = defaultdict(list)
    #contadores
    if request.user.is_authenticated:
        part_count =  Participante.objects.filter(usuario=request.user).count()
        crian_count =  Crianca.objects.filter(usuario=request.user).count()
        pesq_count =  Pesquisa.objects.filter(usuario=request.user).count()

        familia_part = Participante.objects.filter(usuario=request.user)
        familia_kid = Crianca.objects.filter(usuario=request.user)
        
        user_congpais = CustomUser.objects.get(email=request.user)
        if part_count > 0:
            congressoPais = False
            for part in familia_part:
                if part.vai_participar:
                    vai = "Sim"
                    congressoPais = True
                else:
                    vai = "Não"
                argpart={
                    "id":part.id,
                    "nome":"{} {}".format(part.nome,part.sobrenome).strip(),
                    "vai_participar":vai
                }
                args_fam['part'].append(argpart)
            
            if congressoPais:
                user_congpais.congressoPais = True
            else:
                user_congpais.congressoPais = False
            
        else:
            congressoPais = False
            args_fam['part']=None
            user_congpais.congressoPais = False
        
        user_congpais.save()
        
        if crian_count > 0:
            for kid in familia_kid: 
                if kid.vai_participar:
                    vai = "Sim"
                else:
                    vai = "Não"   
                argkid={
                    "id":kid.id,
                    "nome":"{} {}".format(kid.nome,kid.sobrenome).strip(),
                    "vai_participar":vai
                }
                
                args_fam['kid'].append(argkid)
        else:
            args_fam['kid']=None


        form_cadkid = CriancaForm()
        form_cadpart = ParticipanteForm()
        form_editkid = CriancaForm(instance = request.user)
        form_editpart = CriancaForm(instance = request.user)

        args['tem_responsavel'] = congressoPais
        args['form_cadkid'] = form_cadkid
        args['form_cadpart'] = form_cadpart
        args['form_editkid'] = form_cadkid
        args['form_editpart'] = form_editpart          

        args['part_count'] = part_count
        args['crian_count'] = crian_count
        args['pesq_count'] = pesq_count
        args['usuario'] = request.user
    return render(request,'congressoPais_app/index.html',{'info':args, 'familia':args_fam})

@login_required
def cad_crianca(request):
    args={}
    args.update(csrf(request))
    if request.method == 'POST':
        crianca_form = CriancaForm(request.POST)

        if crianca_form.is_valid():
            form = crianca_form.save(commit=False)
            form.usuario = request.user
            form.save()
            return redirect('/congressoPais/')
        else:
            print(form.errors)
    else:
        return render(request,'500.html')

@login_required
def cad_participante(request):
    part_count =  Participante.objects.filter(usuario=request.user).count()
    if part_count == 2:
        return form_invalido(request,'/congressoPais/',
                'O casal já foi cadastrado, mas por ser alterado ainda.')

    if request.method == 'POST':
        form = ParticipanteForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.save()
            return redirect(reverse('congressoPais:index'))
        else:
            print(form.errors)
    else:
        return render(request,'500.html')

@login_required
def cad_editar(request):
    def _editar_cadastro(request, instancia, formulario):
        """
        Retorna uma variacao do formulario na funcao, instanciado,
        com ou sem dados do POST.
        Se aplica apenas aos cadastros de participantes e criancas
        do evento Congresso dos Pais.
        """
        if request.method == 'POST':
            form = formulario(request.POST, instance=instancia)
            if form.is_valid():
                form.save()
            else:
                return form_invalido(request,'/congressoPais/cadastro/editar/')
        else:
            form = formulario(instance=instancia)
        return form

    args = {}
    participante = Participante.objects.filter(usuario=request.user)
    crianca = Crianca.objects.filter(usuario=request.user)
    tipo_edit = request.GET.get('tipo_edit','')
    id_edit = request.GET.get('id_edit','')

    args['form_tipo'] = tipo_edit
    args['id_edit'] = id_edit
    args['participante'] = participante
    args['crianca'] = crianca
    if tipo_edit in ('participante','crianca') and id_edit != '':
        id_edit = int(id_edit)
        if tipo_edit == 'crianca':
            inst_edit = crianca.get(pk=id_edit)
            form = _editar_cadastro(request,inst_edit, CriancaForm)
        else:
            inst_edit = participante.get(pk=id_edit)
            form = _editar_cadastro(request,inst_edit, ParticipanteForm)
        
        if request.method=='POST':
            return redirect('/congressoPais/cadastro/editar/')

        args.update(csrf(request))
    else:
        form = None

    args['form'] = form
    return render(request, 'congressoPais_app/editar.html', args)

def erro404(request):
    return render(request,'404.html')

def erro500(request):
    return render(request,'500.html')