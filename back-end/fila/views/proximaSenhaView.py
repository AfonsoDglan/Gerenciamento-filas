from rest_framework import viewsets
from fila.serializers import SenhasSerializer
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from fila.models import Senha, Painel, Pessoa


class ProximaSenhaViewSet(viewsets.ModelViewSet):
    queryset = Senha.objects.all()
    serializer_class = SenhasSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        if Senha.objects.filter(tipo=2, status=1).count() >= 1:
            utimasDuasSenhasChamadas = Senha.objects.filter(status=1)[::-1][:2]
            if utimasDuasSenhasChamadas[0].tipo != 2 and utimasDuasSenhasChamadas[1].tipo != 2:  # noqa: E501
                proximaSenha = Senha.objects.filter(status=1, tipo=2).first()
                proximaSenha.status = 2
                proximaSenha.save()
                authorization_header = request.data['token']
                print("aquiiiiiiii", authorization_header)
                user_token = authorization_header
                user = Token.objects.get(key=user_token).user
                pessoa = Pessoa.objects.get(user=user)
                sala = pessoa.sala
                chamado = "Senha: " + proximaSenha.senha + "==> Sala: " + sala
                Painel(chamado=chamado, quemChamou=pessoa, horaChamada=timezone.now()).save()  # noqa: E501
                return Response(proximaSenha.senha, status=status.HTTP_200_OK)
            else:
                proximaSenha = Senha.objects.filter(status=1, tipo=1).first()
                print("eiiiiii", proximaSenha)
                proximaSenha.status = 2
                proximaSenha.save()
                authorization_header = request.headers.get('token')
                print("aquiiiiiiii", authorization_header)
                user_token = authorization_header
                user = Token.objects.get(key=user_token).user
                pessoa = Pessoa.objects.get(user=user)
                sala = pessoa.sala
                chamado = "Senha: " + proximaSenha.senha + "==> Sala: " + sala
                Painel(chamado=chamado, quemChamou=pessoa, horaChamada=timezone.now()).save()  # noqa: E501
                return Response(proximaSenha.senha, status=status.HTTP_200_OK)
        elif Senha.objects.filter(status=1).count() >= 1:
            proximaSenha = Senha.objects.filter(status=1, tipo=1).first()
            print("aquiiiiii", proximaSenha)
            proximaSenha.status = 2
            proximaSenha.save()
            authorization_header = request.headers.get('tokentoken')
            print("aquiiiiiiii", request.headers)
            user_token = authorization_header
            user = Token.objects.get(key=user_token).user
            pessoa = Pessoa.objects.get(user=user)
            sala = pessoa.sala
            chamado = "Senha: " + proximaSenha.senha + "==> Sala: " + sala
            Painel(chamado=chamado, quemChamou=pessoa, horaChamada=timezone.now()).save()  # noqa: E501
            return Response(proximaSenha.senha, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
