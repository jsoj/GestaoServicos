from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Product, Manufacturer, Document, Empresa, Origem, Temperatura, Acao, TagPessoa, Pessoa, Status

# Register your models here.
admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Document)
admin.site.register(Empresa)
admin.site.register(Origem)
admin.site.register(Status)
admin.site.register(Temperatura)
admin.site.register(Acao)
admin.site.register(TagPessoa)
admin.site.register(Pessoa)


