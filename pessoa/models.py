from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()


class Pessoa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pessoa', blank=True, null=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
