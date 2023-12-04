from rest_framework import viewsets
from fila.serializers import TriagemSerializer
from rest_framework.response import Response
from rest_framework import status
from fila.models import Triagem


class ProximoPacienteViewSet(viewsets.ModelViewSet):
    queryset = Triagem.objects.all()
    serializer_class = TriagemSerializer

    def list(self, request, *args, **kwargs):
        proximo = Triagem.objects.filter(estado=1).order_by("classificacao").first()  # noqa: E501
        return Response(proximo, status=status.HTTP_200_OK)
        #  return Response(status=satus.HTTP_204_NO_CONTENT)
