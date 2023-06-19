from django.shortcuts import render
from .filters import ProductFilter
from .models import Product
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
            nome_arquivo = str(ultimo.document)   # junior apanhei para descobrir isto.
            df = pd.read_excel(nome_arquivo)
            mydict = {
                "df": df.to_html()
            }
            return render(request, 'upload.html', context=mydict)
    else:
        form = DocumentForm()
    return render(request, "upload.html", {"form": form, "list": list})
