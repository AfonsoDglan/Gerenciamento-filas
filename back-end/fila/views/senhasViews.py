from rest_framework import viewsets
from django.utils import timezone
from fila.serializers import SenhasSerializer
from rest_framework.response import Response
from rest_framework import status
from fila.models import Senha


class SenhasViewSet(viewsets.ModelViewSet):
    queryset = Senha.objects.all()
    serializer_class = SenhasSerializer

    def list(self, request, *args, **kwargs):
        if request.GET.get('tipo') == "p":
            ultimaSenha = Senha.objects.filter(tipo=2).count()
            senha = 'P - ' + str(ultimaSenha+1)
            request.session['senha'] = senha
            Senha.objects.create(senha=senha, status=1, horaEmitida=timezone.now(), tipo=2)  # noqa: E501
            return Response(senha, status=status.HTTP_201_CREATED)
        ultimaSenha = Senha.objects.filter(tipo=1).count()
        senha = 'C - ' + str(ultimaSenha+1)
        request.session['senha'] = senha
        Senha.objects.create(senha=senha, status=1, horaEmitida=timezone.now(), tipo=1)  # noqa: E501
        return Response(senha, status=status.HTTP_201_CREATED)
