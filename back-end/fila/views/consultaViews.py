from rest_framework import viewsets
from fila.serializers import ConsultaSerializer
from fila.models import Consulta


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
