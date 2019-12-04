from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    '''
    ModelViewSet para Avaliacao
    '''
    http_method_names = ['get', 'post']
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(AvaliacaoViewSet, self).get_queryset()

        id_receita = self.request.query_params.get('id_receita', None)
        if id_receita:
            queryset = queryset.filter(receita_id=id_receita)

        return queryset