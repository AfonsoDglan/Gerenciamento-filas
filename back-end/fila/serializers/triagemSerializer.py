from rest_framework import serializers
from fila.models import Triagem


class TriagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triagem
        fields = '__all__'
        extra_kwargs = {
            'atendente': {'read_only': True},
            'estado': {'read_only': True},
            'senha': {'read_only': True},
            'classificacao': {'read_only': True},
        }
