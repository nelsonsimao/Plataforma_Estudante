from django.conf.urls import patterns, url

from alojamentos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'(?P<pk>\d+)/$', views.descricaoAlugo, name='descricaoAlugo'),
    url(r'adicionar_alojamento/$', views.adicionarAlojamento, name='adicionarAlojamento'),
)
