from rest_framework import serializers
from fila.models import Consulta


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ["diagnostico"]
