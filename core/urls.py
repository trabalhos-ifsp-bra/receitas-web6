from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    index,
    nova_receita,
    detalhes_receita
)

app_name = "core"

urlpatterns = [
    path('', index, name='index'),
    path('receitas/nova/', nova_receita, name='nova_receita'),
    path('receitas/detalhes/<int:pk>/', detalhes_receita, name='detalhes_receita'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
