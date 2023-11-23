from rest_framework.routers import DefaultRouter
from django.urls import path
from fila.views.senhasViews import SenhaViewSet
from django.http import HttpResponse


router = DefaultRouter()
router.register("senhas", SenhaViewSet, basename="senha")

urlpatters = router.urls

def teste(request):
   return HttpResponse("teste")
urlpatterns = [
    path("", teste),
]
urlpatterns += router.urls