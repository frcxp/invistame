from django.shortcuts import render, redirect, HttpResponse
from .models import Investimentos
from .forms import InvestimentosForm
from django.contrib.auth.decorators import login_required


def pagina_de_investimentos(request):
    dados = {
        'dados':Investimentos.objects.all()
    }
    return render(request, 'investimentos/pagina_de_investimentos.html', context=dados)

@login_required
def detalhe(request,id_investimento):
    dados = {
        'dados': Investimentos.objects.get(pk=id_investimento)
        }
    return render(request,'investimentos/detalhe.html',dados)

@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentosForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('pagina_de_investimentos')
    else:
        investimento_form = InvestimentosForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)



@login_required
def editar(request, id_investimento):
    investimento = Investimentos.objects.get(pk=id_investimento)
    # novo_investimento/1 -> GET
    if request.method == 'GET':
        formulario = InvestimentosForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    # caso requisição seja POST
    else:
        formulario = InvestimentosForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('pagina_de_investimentos')



@login_required
def excluir(request, id_investimento):
    investimento = Investimentos.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('pagina_de_investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html',{'item': investimento})
