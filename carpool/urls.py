from django.conf.urls import patterns, url

from carpool import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'(?P<pk>\d+)/$', views.descricaoBoleia, name='descricaoBoleia'),
    url(r'adicionar_boleia/$', views.adicionarBoleia, name='adicionarBoleia'),
)
