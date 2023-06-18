from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from perfil.models import RedeSocial, Endereco, Localizacao

Usuario = get_user_model()


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        # fields = '__all__'
        fields = ['id', 'tipo', 'cep', 'lugradouro', 'numero', 'bairro', 'cidade', 'estado', 'uf', 'pais']


class RedeSocialSerializer(ModelSerializer):
    class Meta:
        model = RedeSocial
        fields = ['whatsapp', 'instagram', 'facebook', 'twitter', 'youtube', 'linkedin', 'github', 'discord', ]


class LocalizacaoSerializer(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['latitude', 'longitude']


class PerfilSerializer(ModelSerializer):
    nome = serializers.CharField(source='first_name')
    sobrenome = serializers.CharField(source='last_name')
    redes_sociais = RedeSocialSerializer(source='redesocial')
    enderecos = EnderecoSerializer(many=True, source='endereco_set')
    localizacao = LocalizacaoSerializer()

    class Meta:
        model = Usuario
        fields = ['id', 'foto', 'nome', 'sobrenome', 'email', 'celular', 'enderecos', 'redes_sociais', 'localizacao']
