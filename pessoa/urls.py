from django.urls import include, path
from rest_framework import routers
from perfil.api.viewsets import PerfilViewSet, RedeSocialViewSet, EnderecoViewSet, LocalizacaoViewSet
from pessoa.api.viewsets import PessoaViewSet

router = routers.DefaultRouter()
router.register('', PessoaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
