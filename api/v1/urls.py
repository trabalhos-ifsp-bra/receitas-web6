from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AvaliacaoViewSet, FavoritoViewSet, ComentarioViewSet

app_name='v1'

router = routers.SimpleRouter()
router.register('avaliacoes', AvaliacaoViewSet, base_name='avaliacao'),
router.register('favoritos', FavoritoViewSet, base_name='favorito'),
router.register('comentarios', ComentarioViewSet, base_name='comentario')


urlpatterns = router.urls