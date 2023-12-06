from rest_framework import viewsets
from fila.serializers import PainelSerializer
from fila.models import Painel


class PainelViewSet(viewsets.ModelViewSet):
    queryset = Painel.objects.all()[:5]
    serializer_class = PainelSerializer
