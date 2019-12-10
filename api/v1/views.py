from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Avaliacao, Favorito, Comentario
from .serializers import AvaliacaoSerializer, FavoritoSerializer, ComentarioSerializer

class AvaliacaoViewSet(ModelViewSet):
    '''
    ModelViewSet para Avaliacao
    '''
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()

    def get_queryset(self):
        queryset = super(AvaliacaoViewSet, self).get_queryset()

        id_receita = self.request.query_params.get('id_receita', None)
        if id_receita:
            queryset = queryset.filter(receita_id=id_receita)

        return queryset

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

class FavoritoViewSet(ModelViewSet):
    '''
    ModelViewSet para Favorito
    '''
    serializer_class = FavoritoSerializer
    queryset = Favorito.objects.all()

    def get_queryset(self):
        queryset = super(FavoritoViewSet, self).get_queryset()
        if self.request.user:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

class ComentarioViewSet(ModelViewSet):
    '''
    ModelViewSet para Favorito
    '''
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()

    def get_queryset(self):
        queryset = super(ComentarioViewSet, self).get_queryset()
        if self.request.user:
            queryset = queryset.filter(autor=self.request.user)
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save(autor=self.request.user)