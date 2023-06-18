from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

Usuario = get_user_model()


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label="Email")
    senha = serializers.CharField(label="Senha", style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('senha')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)

            if not user:
                msg = 'E-mail ou senha, estão incorretos. Tente outra vez.'
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Você deve incluir e-mail e senha".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class MudarSenhaSerializer(serializers.Serializer):
    senha_atual = serializers.CharField(required=True)
    senha_nova = serializers.CharField(required=True)

    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Senha atual incorreta.')
        return value

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['senha_nova'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = Usuario

    senha_atual = serializers.CharField(required=True)
    senha_nova = serializers.CharField(required=True)
