from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet

from perfil.api.serializers import PerfilSerializer, RedeSocialSerializer, LocalizacaoSerializer, EnderecoSerializer
from perfil.models import Endereco, Localizacao, RedeSocial

Usuario = get_user_model()


class PerfilViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = Usuario.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get_object(self):
        return self.queryset.get(email=self.request.user)


class RedeSocialViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = RedeSocial.objects.all()
    serializer_class = RedeSocialSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get_object(self):
        return self.queryset.get(usuario=self.request.user)


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)


class LocalizacaoViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get_object(self):
        return self.queryset.get(usuario=self.request.user)


class PerfilTesteViewSet(ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
