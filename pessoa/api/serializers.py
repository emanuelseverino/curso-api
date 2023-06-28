from django.contrib.auth import authenticate, get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from perfil.models import RedeSocial, Endereco, Localizacao
from pessoa.models import Pessoa

Usuario = get_user_model()


class PessoaSerializer(ModelSerializer):
    foto = Base64ImageField(required=False)

    def create(self, validated_data):
        pessoa = Pessoa(**validated_data)
        pessoa.usuario = self.context['request'].user
        pessoa.save()
        return pessoa

    class Meta:
        model = Pessoa
        fields = ['id', 'foto', 'nome', 'email', 'idade', ]
        ordering = ['nome', ]
