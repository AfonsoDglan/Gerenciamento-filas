from rest_framework import viewsets
from fila.serializers import PessoaSerializer
from fila.models import Pessoa


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
