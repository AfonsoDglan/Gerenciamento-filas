from rest_framework import viewsets
from fila.serializers import SenhasSerializer
from rest_framework.response import Response
from rest_framework import status
from fila.models import Senha


class SenhaPrioritariaViewSet(viewsets.ModelViewSet):
    queryset = Senha.objects.all()
    serializer_class = SenhasSerializer

    def list(self, request, *args, **kwargs):
        ultimaSenha = Senha.objects.filter(tipo=2).count()
        senha = 'P - ' + str(ultimaSenha+1)
        request.session['senha'] = senha
        Senha.objects.create(senha=senha, status=2, tipo=2)
        return Response(senha, status=status.HTTP_201_CREATED)
