from rest_framework.routers import DefaultRouter
from django.urls import path
from fila.views import (SenhasViewSet, ProximaSenhaViewSet,
                        ProximoPacienteViewSet, TriagemViewSet,
                        PessoaViewSet, PainelViewSet,
                        ConsultaViewSet)
from django.http import HttpResponse


router = DefaultRouter()
router.register("triagem", TriagemViewSet, basename="triagem")
router.register("pessoa", PessoaViewSet, basename="pessoa")
router.register("painel", PainelViewSet, basename="painel")
router.register("consulta", ConsultaViewSet, basename="consulta")
router.register("proxima", ProximaSenhaViewSet, basename="proxima")
router.register("proximopaciente", ProximoPacienteViewSet, basename="proxpac")
urlpatters = router.urls


def teste(request):
    return HttpResponse("teste")


urlpatterns = [
    path("", teste),
    path("senha/", SenhasViewSet.as_view({'get': 'list'})),
]
urlpatterns += router.urls
