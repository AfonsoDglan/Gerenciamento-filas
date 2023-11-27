from rest_framework import viewsets
from fila.serializers import TriagemSerializer
from fila.models import Triagem


class TriagemViewSet(viewsets.ModelViewSet):
    queryset = Triagem.objects.all()
    serializer_class = TriagemSerializer
