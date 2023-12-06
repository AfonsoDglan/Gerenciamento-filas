from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from fila.models import Pessoa
from fila.serializers import PessoaSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = PessoaSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['user']['username'],
                password=serializer.validated_data['user']['password']
            )
            profile_data = {
                'user': user,
                'cpf': serializer.validated_data['cpf'],
                'nomeCompleto': serializer.validated_data['nomeCompleto'],
                'tipo': serializer.validated_data['tipo'],
                'sala': serializer.validated_data['sala'],
            }
            Pessoa.objects.create(**profile_data)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)  # noqa: E501
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  # noqa: E501
