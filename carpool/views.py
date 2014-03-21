from carpool.models import OfereceBoleia
from django.forms.models import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from accounts.models import MyProfile
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    latest_carpool_list = OfereceBoleia.objects.order_by('-pub_data')
    template = loader.get_template('carpool/index_carpool.html')
    context = Context({
        'latest_carpool_list': latest_carpool_list,
    })
    return HttpResponse(template.render(context))

@login_required
def descricaoBoleia(request, pk):
    boleia = OfereceBoleia.objects.get(pk=pk)
    context = Context({
        'boleia': boleia,
    })
    return render(request,'carpool/info.html',context)

@login_required
def adicionarBoleia(request):
    formulario = modelform_factory(OfereceBoleia, exclude=['pub_data', 'userNameC'])
    user = MyProfile.objects.get(user=request.user)
    if request.POST:
        formulario = formulario(request.POST)
        if formulario.is_valid():
            novoCarpool = formulario.save(commit=False)  #aqui faz um pre-save do formulario
            novoCarpool.userNameC = user                  #adiciona o userName ao formulario
            novoCarpool.save()                           #faz save do formulario
            return HttpResponseRedirect('/carpool')
    return render(request, 'carpool/adicionar_boleia.html', {'form': formulario})