from django.contrib import admin
from django.db import models
from .models import Receita, Comentario, Categoria, Favorito, Avaliacao
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
    
    def save_model(self, request, obj, form, change):
    # associating the current logged in user to the client_id
        obj.autor = request.user
        super().save_model(request, obj, form, change)

class AvaliacaoAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        qs = super(AvaliacaoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    
    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ('user', )
            self.readonly_fields=('receita',)
        form = super(AvaliacaoAdmin, self).get_form(request, obj, **kwargs)
        return form



class CategoriaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(CategoriaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ("user")
        form = super(CategoriaAdmin, self).get_form(request, obj, **kwargs)
        return form

class ComentarioAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ComentarioAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ('autor', )
            self.readonly_fields=('receita',)
        form = super(ComentarioAdmin, self).get_form(request, obj, **kwargs)
        return form

class FavoritoAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(FavoritoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ("user")
        form = super(FavoritoAdmin, self).get_form(request, obj, **kwargs)
        return form

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Favorito, FavoritoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
