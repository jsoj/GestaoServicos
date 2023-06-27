from django.db import models


class Manufacturer(models.Model):
    nome = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='filesupload')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    ativo = models.BooleanField(default=True)


class Origem(models.Model):
    origem = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)


class Status(models.Model):
    categoria_status = models.CharField(max_length=25)
    ativo = models.BooleanField(default=True)


class Temperatura(models.Model):
    temperatura = models.CharField(max_length=10)
    ativo = models.BooleanField(default=True)


class Acao(models.Model):
    acao = models.CharField(max_length=25)
    ativo = models.BooleanField(default=True)


class TagPessoa(models.Model):
    tagpessoa = models.CharField(max_length=10)
    ativo = models.BooleanField(default=True)


class Pessoa(models.Model):
    nome = models.CharField(max_length=25, blank=False, verbose_name="Nome")
    telefone = models.CharField(max_length=25, blank=False, unique=True, verbose_name="Telefone")
    data_entrada = models.DateField(auto_now_add=True, blank=False, verbose_name="Data de Entrada")
    origem = models.ForeignKey(Origem, on_delete=models.CASCADE, verbose_name="Origem do Lead")
    categoria_status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Status da Pessoa")
    temperatura = models.ForeignKey(Temperatura, on_delete=models.CASCADE, verbose_name="Temperatura")
    tag = models.ManyToManyField(TagPessoa, verbose_name="Tag")
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, verbose_name="Próximos Passos")
    ativo = models.BooleanField(default=True)
