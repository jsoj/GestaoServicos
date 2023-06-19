from django.urls import path
from . import views
from django_filters.views import FilterView
from crm.models import Product

urlpatterns = [
    path('',        views.index,        name="index"),
    path('list/',   views.product_list, name="product-list"),
    path('index/',  views.index,        name="index"),
    path('upload/',  views.upload,        name="upload"),
]

