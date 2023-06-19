import django_filters
from .models import Product


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