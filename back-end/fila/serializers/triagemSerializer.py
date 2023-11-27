from rest_framework import serializers
from fila.models import Triagem


class TriagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triagem
        fields = ["nomePaciente", "sexo", "queixaPrincipal", "historicoBreve",
                  "observacaoObjetiva", "dor", "frequenciaCardiaca",
                  "frequenciaRespiratoria", "pressaoArterial", "temperatura",
                  "fraturasExpostas", "quimadurasGraves"]
