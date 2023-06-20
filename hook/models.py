from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()

STATUS_CHOICES = [
    ("pending", "Pendente"),
    ("approved", "Aprovado"),
    ("cancelled", "Cancelado"),
]


class Pagamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pagamento_id = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    status_detalhe = models.CharField(max_length=30, null=True, blank=True)
    criado_em = models.CharField(max_length=30, null=True, blank=True)
    atualizado_em = models.CharField(max_length=30, null=True, blank=True)
    pago_em = models.CharField(max_length=30, null=True, blank=True)
    descricao = models.CharField(max_length=30, null=True, blank=True)
    qr_code = models.CharField(max_length=10000, null=True, blank=True)
    qr_code64 = models.CharField(max_length=6000, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '%s - %s | %s' % (self.usuario, self.pagamento_id, self.status)


class MercadoPago(models.Model):
    action = models.CharField(max_length=30)
    api_version = models.CharField(max_length=30)
    application_id = models.CharField(max_length=30)
    date_created = models.CharField(max_length=30)
    id_web = models.CharField(max_length=30)
    live_mode = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    data = models.CharField(max_length=30)

    def __str__(self):
        return '%s - %s' % (self.pk, self.id_web)


class Teste(models.Model):
    usuario = models.CharField(max_length=100, blank=True, null=True)
    mensagem = models.CharField(max_length=10000)

    def __str__(self):
        return '%s - %s' % (self.usuario, self.mensagem)


class Cobranca(models.Model):
    id_web = models.CharField(max_length=50, null=True, blank=True)
    mensagem = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.id_web, self.mensagem)
