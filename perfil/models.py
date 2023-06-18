from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()


class Endereco(models.Model):
    TIPO_CHOICES = [
        ("CASA", "Casa"),
        ("TRABALHO", "Trabalho"),
        ("OUTROS", "Outros"),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default="OUTROS")
    cep = models.CharField(max_length=20, blank=True, null=True)
    lugradouro = models.CharField(max_length=200, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.usuario, self.tipo)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class RedeSocial(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    whatsapp = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    discord = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '%s' % self.usuario

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'


class Localizacao(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '%s' % self.usuario

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'
