from django.shortcuts import render
from .filters import ProductFilter, EmpresaFilter, TagFilter, OrigemFilter, AcaoFilter, StatusFilter, PessoaFilter, \
    TemperaturaFilter
from .models import Product, Empresa, Pessoa, Origem, Temperatura, Acao, TagPessoa, Status
from .models import Document
from .forms import DocumentForm
import pandas as pd
from os import path


# Create your views here.

def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'list.html', {'filter': f})


def index(request):
    return render(request, 'index.html')


def upload(request):
    list = Document.objects.all()
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            ultimo = Document.objects.last()
            nome_arquivo = str(ultimo.document)  # junior apanhei para descobrir isto.
            df = pd.read_excel(nome_arquivo)
            mydict = {
                "df": df.to_html()
            }
            return render(request, 'upload.html', context=mydict)
    else:
        form = DocumentForm()
    return render(request, "upload.html", {"form": form, "list": list})


def tabela(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'Tabela.html', {'filter': f})


def empresa(request):
    f = EmpresaFilter(request.GET, queryset=Empresa.objects.all())
    return render(request, 'Tabela.html', {'filter': f})


def pessoa(request):
    f = PessoaFilter(request.GET, queryset=Pessoa.objects.all())
    return render(request, 'Tabela.html', {'filter': f})


def origem(request):
    f = OrigemFilter(request.GET, queryset=Origem.objects.all())
    return render(request, 'Tabela.html', {'filter': f})


def temperatura(request):
    f = TemperaturaFilter(request.GET, queryset=Temperatura.objects.all())
    return render(request, 'Tabela.html', {'filter': f})


def acao(request):
    f = AcaoFilter(request.GET, queryset=Acao.objects.all())
    return render(request, 'Tabela.html', {'filter': f})


def tagpessoa(request):
    f = TagFilter(request.GET, queryset=TagPessoa.objects.all())
    return render(request, 'Tabela.html', {'filter': f})


def status(request):
    f = StatusFilter(request.GET, queryset=Status.objects.all())
    return render(request, 'Tabela.html', {'filter': f})
