from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Receita


# Create the form class.
class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'imagem', 'descricao', 'categoria','tempo']

    def __init__(self, *args, **kwargs):
        self.autor = kwargs.pop('user', None)
        super(ReceitaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(ReceitaForm, self).save(commit=False)
        obj.autor = self.autor
        if commit:
            obj.save()
        return obj