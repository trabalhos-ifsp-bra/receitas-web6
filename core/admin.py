from django.contrib import admin
from .models import Receita, Comentario, Categoria, Favorito
from django_summernote.admin import SummernoteModelAdmin


class ReceitaAdmin(SummernoteModelAdmin):
    pass


admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Comentario)
admin.site.register(Favorito)
admin.site.register(Categoria)
