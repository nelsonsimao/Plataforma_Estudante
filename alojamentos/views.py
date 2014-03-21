from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader

from alojamentos.models import AlugoCasa
from django.shortcuts import render
from django.forms.models import modelform_factory
from accounts.models import MyProfile
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    latest_alojamentos_list = AlugoCasa.objects.order_by('-pub_data')
    template = loader.get_template('alojamentos/index_alojamentos.html')
    context = Context({
        'latest_alojamentos_list': latest_alojamentos_list,
    })
    return HttpResponse(template.render(context))

@login_required
def descricaoAlugo(request, pk):
    alojamento = AlugoCasa.objects.get(pk=pk)
    context = Context({
        'alojamento': alojamento,
    })
    return render(request,'alojamentos/info.html',context)

@login_required
def adicionarAlojamento(request):
    formulario = modelform_factory(AlugoCasa, exclude=['pub_data', 'userName'])
    user = MyProfile.objects.get(user=request.user)
    if request.POST:
        formulario = formulario(request.POST)
        if formulario.is_valid():
            novoAlojamento = formulario.save(commit=False)  #aqui faz um pre-save do formulario
            novoAlojamento.userName = user                  #adiciona o userName ao formulario
            novoAlojamento.save()                           #faz save do formularioa
            return HttpResponseRedirect('/alojamentos')
    return render(request, 'alojamentos/adicionar_alojamento.html', {'form': formulario})