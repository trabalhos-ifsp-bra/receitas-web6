from django.contrib import admin
from django.db import models
from .models import Receita, Comentario, Categoria, Favorito
from django import forms
from django_summernote.widgets import SummernoteWidget

class ReceitaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget(attrs={'width': '50%', 'height': '100%'})},
    }
    
    def get_queryset(self, request):
        qs = super(ReceitaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ("rating", "autor")
        form = super(ReceitaAdmin, self).get_form(request, obj, **kwargs)
        return form

class CategoriaAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        fields = super(CategoriaAdmin, self).get_fields(request, obj)
        for field in fields:
            if field == 'slug' and obj is None:
                continue
            yield field

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Comentario)
admin.site.register(Favorito)
admin.site.register(Categoria, CategoriaAdmin)
