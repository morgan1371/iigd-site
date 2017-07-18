from django.conf.urls import url, include
from django.contrib import admin
from congressoPais_app import views
from django.conf.urls import handler404, handler500

app_name = 'congressoPais'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    
    #cadastrar para o evento
    url(r'^cadastrar/participante/$',views.cad_participante, name='cad_participante'),
    url(r'^cadastrar/crianca/$',views.cad_crianca, name='cad_crianca'),
    
    #editar cadastro para o evento
    url(r'^cadastro/editar/$', views.cad_editar, name='cad_editar'),
    url(r'^cadastro/editar/(?P<tipo_edit>)&(?P<id_edit>)/$', views.cad_editar, name='cad_editar')
]

handler404 = views.erro404
handler500 = views.erro500