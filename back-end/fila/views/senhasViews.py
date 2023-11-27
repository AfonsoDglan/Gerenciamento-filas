from rest_framework import viewsets
from fila.serializers import SenhasSerializer
from fila.models import Senha


class SenhaViewSet(viewsets.ModelViewSet):
    queryset = Senha.objects.all()
    serializer_class = SenhasSerializer
