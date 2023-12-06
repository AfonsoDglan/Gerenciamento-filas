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
            serializer.validated_data['atendente'] = Pessoa.objects.get(user__username=request.user)  # noqa: E501
            serializer.validated_data['estado'] = 1
            fratura = serializer.validated_data['fraturasExpostas']
            queimadura = serializer.validated_data['quimadurasGraves']
            frequenciacard = serializer.validated_data['frequenciaCardiaca']
            frequenciaresp = serializer.validated_data['frequenciaRespiratoria']  # noqa: E501
            pressaoart = serializer.validated_data['pressaoArterial']
            temperatura = serializer.validated_data['temperatura']
            dor = serializer.validated_data['dor']
            classificacao = self.classificar(fratura, queimadura,
                                             frequenciacard, frequenciaresp,
                                             pressaoart, temperatura, dor)
            serializer.validated_data['classificacao'] = classificacao
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def fraturasExpostas(self, fratura):
        return 100 if fratura == 1 else 0

    def quimadurasGraves(self, queimadura):
        return 100 if queimadura == 1 else 0

    def frequenciaCardiaca(self, frequenciacard):
        if frequenciacard >= 60 and frequenciacard <= 100:
            return 0
        elif frequenciacard < 60 and frequenciacard >= 0:
            return 20
        elif frequenciacard > 100:
            return 30
        else:
            return 0

    def frequenciaRespiratoria(self, frequenciaresp):
        if frequenciaresp >= 12 and frequenciaresp <= 20:
            return 0
        elif frequenciaresp < 12 and frequenciaresp >= 0:
            return 30
        elif frequenciaresp > 20:
            return 20
        else:
            return 0

    def pressaoArterial(sef, pressaoart):
        ops = {1: 0,
               2: 15,
               3: 20,
               4: 25,
               5: 30}
        return ops[pressaoart]

    def temperatura(self, temperatura):
        if temperatura > 38 or temperatura < 35:
            return 30
        else:
            return 0

    def classificar(self, fratura, queimadura, frequenciacard, frequenciaresp, pressaoart, temperatura, dor):  # noqa : E501
        pontos = 0
        pontos += self.fraturasExpostas(fratura)
        pontos += self.quimadurasGraves(queimadura)
        pontos += self.frequenciaCardiaca(frequenciacard)
        pontos += self.frequenciaRespiratoria(frequenciaresp)
        pontos += self.pressaoArterial(pressaoart)
        pontos += self.temperatura(temperatura)
        pontos += dor
        if pontos >= 100:
            return 1
        elif pontos >= 90:
            return 2
        elif pontos >= 70:
            return 3
        elif pontos >= 50:
            return 4
        else:
            return 5
