from rest_framework import serializers
from fila.models import Painel


class PainelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painel
        fields = ["senha", "sala"]
