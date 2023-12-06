from rest_framework import serializers
from django.contrib.auth.models import User
from fila.models import Pessoa


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class PessoaSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Pessoa
        fields = "__all__"
