from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from home_app.forms import CustomUserCreationForm
from home_app.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.utils import timezone as tz

# Create your views here.

def index(request):
    return render(request,'home_app/index.html')

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,'home_app/login.html',c)


def auth_view(request):
    usuario = request.POST.get('usuario','')
    senha = request.POST.get('senha','')
    usu = auth.authenticate(username=usuario, password=senha)

    if usu is not None:
        auth.login(request,usu)
        return HttpResponseRedirect(reverse('home:index'))
    else:
        return HttpResponseRedirect('/contas/invalido')

@login_required
def login_valido(request):
    return render(request, 'home_app/login_valido.html',
                  {'usuario':request.user})


def login_invalido(request):
        return render(request, 'home_app/login_invalido.html',{'user':request.user})

@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'home_app/logout.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contas/registrado')
    else:
        form = CustomUserCreationForm()
    args={}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'home_app/registrar.html', args)

def registrar_valido(request):
    return render(request, 'home_app/registrar_valido.html')

@login_required
def usuario_edit(request):
    inst = CustomUser.objects.get(email=request.user)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance = inst)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contas/registrado')
    else:
        form = CustomUserCreationForm(instance = inst)
    
    args={}
    args.update(csrf(request))

    args['form'] = form
    return render(request, 'home_app/editar.html', args)


def erro404(request):
    return render(request,'404.html')

def erro500(request):
    return render(request,'500.html')