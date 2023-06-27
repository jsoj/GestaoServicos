import django_filters
from .models import Product, Pessoa, Temperatura, Acao, TagPessoa, Origem, Status, Empresa


class ProductFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    release_year__gt = django_filters.DateFilter(field_name='release_date', lookup_expr='year__gt')
    release_year__lt = django_filters.DateFilter(field_name='release_date', lookup_expr='year__lt')
    manufacturer__nome = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')

    # class Meta:
    #     model = Product
    #     fields = ['price', 'release_date', 'manufacturer']


class PessoaFilter(django_filters.FilterSet):
    class Meta:
        model = Pessoa
        fields = ['nome', 'telefone']



class EmpresaFilter(django_filters.FilterSet):
    class Meta:
        model = Empresa
        fields =['nome', 'cnpj']


class OrigemFilter(django_filters.FilterSet):
    class Meta:
        model = Origem
        fields = ['origem']


class CategoriaStatusFilter(django_filters.FilterSet):
    class Meta:
        model = Status
        fields =['categoria_status']


class OrigemFilter(django_filters.FilterSet):
    class Meta:
        model = Origem
        fields = ['origem']


class TagFilter(django_filters.FilterSet):
    class Meta:
        model = TagPessoa
        fields = ['tagpessoa']


class AcaoFilter(django_filters.FilterSet):
    class Meta:
        model = Acao
        fields = ['acao']

class PessoaFilter(django_filters.FilterSet):
    class Meta:
        model = Pessoa
        fields = ['nome', 'telefone', 'temperatura']


class TemperaturaFilter(django_filters.FilterSet):
    class Meta:
        model = Temperatura
        fields = ['temperatura']

class StatusFilter(django_filters.FilterSet):
    class Meta:
        model = Status
        fields = ['categoria_status']