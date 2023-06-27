from django.urls import path
from . import views

urlpatterns = [
    path('',                views.index,        name="index"),
    path('list/',           views.product_list, name="product-list"),
    path('index/',          views.index,        name="index"),
    path('upload/',         views.upload,        name="upload"),
    path('tabela/',         views.tabela,        name="tabela"),
    path('origem/',         views.origem,       name="origem"),
    path('status/',         views.status,       name="status"),
    path('pessoa/',         views.pessoa,       name="pessoa"),
    path('temperatura/',    views.temperatura,  name="temperatura"),
    path('acao/',           views.acao,         name="acao"),
    path('tagpessoa/',      views.tagpessoa,    name="tagpessoa"),
    path('empresa/',        views.empresa,       name="empresa"),

]

