from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from fila.serializers import TriagemSerializer
from fila.models import Triagem, Pessoa


class TriagemViewSet(viewsets.ModelViewSet):
    queryset = Triagem.objects.all()
    serializer_class = TriagemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['atendente'] = Pessoa.objects.get(user__username=request.user)
            serializer.validated_data['estado'] = 2
            serializer.validated_data['senha'] = "senha1"
            serializer.validated_data['classificacao'] = 5
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
