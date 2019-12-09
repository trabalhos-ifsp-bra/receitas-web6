from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import core.views as views
from django.conf.urls import  include
from django.contrib import admin

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', admin.site.urls, name='admin'),
    path('<str:categoria>', views.index, name='index'),
    path('receitas/nova/', views.nova_receita, name='nova_receita'),
    path('receitas/detalhes/<int:pk>/', views.detalhes_receita, name='detalhes_receita'),
    path('receitas/detalhes/<int:pk>/<str:fav>/', views.detalhes_receita, name='favoritar'),
    path('favoritos/', views.favoritos, name='favoritos')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
