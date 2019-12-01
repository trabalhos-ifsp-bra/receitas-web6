from rest_framework import serializers
from core.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    '''
    ModelSerializer for Avaliacao model
    '''

    class Meta:
        model = Avaliacao
        fields = '__all__'