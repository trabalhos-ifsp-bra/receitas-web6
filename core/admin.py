from django.contrib import admin
from .models import Receita, Comentario, Categoria, Favorito
from django_summernote.admin import SummernoteModelAdmin


class ReceitaAdmin(SummernoteModelAdmin):
    pass

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
