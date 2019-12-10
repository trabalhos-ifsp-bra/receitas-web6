from rest_framework import serializers
from core.models import Avaliacao, Favorito, Comentario


class AvaliacaoSerializer(serializers.ModelSerializer):
    '''
    ModelSerializer for Avaliacao model
    '''

    class Meta:
        model = Avaliacao
        fields = '__all__'
        extra_kwargs = {
            'user' : {'read_only' : True }
        }

class FavoritoSerializer(serializers.ModelSerializer):
    '''
    ModelSerializer for Avaliacao model
    '''

    class Meta:
        model = Favorito
        fields = '__all__'
        extra_kwargs = {
            'user' : {'read_only' : True }
        }

class ComentarioSerializer(serializers.ModelSerializer):
    '''
    ModelSerializer for Avaliacao model
    '''

    class Meta:
        model = Comentario
        fields = '__all__'
        extra_kwargs = {
            'autor' : {'read_only' : True }
        }