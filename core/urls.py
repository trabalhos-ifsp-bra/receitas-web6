from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import core.views as views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:categoria>', views.index, name='index'),
    path('receitas/nova/', views.nova_receita, name='nova_receita'),
    path('receitas/detalhes/<int:pk>/', views.detalhes_receita, name='detalhes_receita')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
