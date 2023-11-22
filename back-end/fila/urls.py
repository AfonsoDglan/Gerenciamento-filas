from rest_framework.routers import DefaultRouter
from fila.views.senhasViews import SenhaViewSet

router = DefaultRouter()
router.register("senhas", SenhaViewSet, basename="senha")

urlpatters = router.urls
urlpatters += [
       
]