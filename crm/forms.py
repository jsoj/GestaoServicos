from django import forms
from django.forms import ModelForm

from .models import Document, Empresa, Pessoa, Origem, Status, Acao, TagPessoa, Temperatura


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = "__all__"


class OrigemForm(ModelForm):
    class Meta:
        model = Origem
        fields = "__all__"


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = "__all__"


class OrigemForm(ModelForm):
    class Meta:
        model = Origem
        fields = "__all__"


class TagForm(ModelForm):
    class Meta:
        model = TagPessoa
        fields = "__all__"


class AcaoForm(ModelForm):
    class Meta:
        model = Acao
        fields = "__all__"


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = "__all__"


class TemperaturaForm(ModelForm):
    class Meta:
        model = Temperatura
        fields = "__all__"
