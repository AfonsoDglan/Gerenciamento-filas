from rest_framework import serializers
from models.senhas import Senha

class SenhasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senha
        fields = ['senha','status', 'tipo']