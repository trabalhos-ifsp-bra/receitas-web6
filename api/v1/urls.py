from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AvaliacaoViewSet

app_name='v1'

router = routers.SimpleRouter()
router.register('avaliacoes', AvaliacaoViewSet, base_name='avaliacao')

urlpatterns = router.urls