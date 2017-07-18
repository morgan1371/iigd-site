from django.conf.urls import url, include
from django.contrib import admin
from home_app import views
from django.conf.urls import handler404, handler500

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #auth
    url(r'^contas/entrar/$', views.login, name='entrarConta'),
    url(r'^contas/auth/$', views.auth_view),
    url(r'^contas/logout/$', views.logout, name='sairConta'),
    url(r'^contas/valido/$', views.login_valido),
    url(r'^contas/invalido/$', views.login_invalido),
    url(r'^contas/registrar/$', views.registrar_usuario, name='criarConta'),
    url(r'^contas/registrado/$', views.registrar_valido),
    url(r'^contas/editar/$', views.usuario_edit, name='editar'),
]

handler404 = views.erro404
handler500 = views.erro500