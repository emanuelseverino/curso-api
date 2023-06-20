import datetime

import requests
import json

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from hook.models import Cobranca, Pagamento, MercadoPago, Teste

Usuario = get_user_model()


class PagarView(LoginRequiredMixin, View):
    login_url = '/contas/login'

    def get(self, request, *args, **kwargs):
        return render(request, 'pagamento/pagar.html')

    def post(self, request, *args, **kwargs):
        data = {
            "transaction_amount": 1,
            "description": "Testando a API",
            "payment_method_id": "pix",
            "payer": {
                "email": self.request.user.email,
                "first_name": self.request.user.first_name,
                "last_name": self.request.user.last_name,
                "identification": {
                    "type": "CPF",
                    "number": self.request.POST.get('cpf').replace('.', '').replace('-', '')
                },
                "address": {
                    "zip_code": "28300000",
                    "street_name": "Rua Maria Otalia Boechat",
                    "street_number": "177",
                    "neighborhood": "Aeroporto",
                    "city": "Itaperuna",
                    "federal_unit": "RJ"
                }
            }
        }
        headers = {
            'Authorization': 'Bearer APP_USR-7893702088637531-012618-cd9f06ef47c005273a3cd983a2ce2902-119438936',
        }

        response = requests.post('https://api.mercadopago.com/v1/payments', json=data, headers=headers)

        data = json.loads(response.content)

        if response.status_code == 201:
            cob = Pagamento.objects.create(
                usuario=self.request.user,
                pagamento_id=data['id'], status=data['status'],
                status_detalhe=data['status_detail'],
                criado_em=data['date_created'], atualizado_em=data['status'],
                pago_em=data['date_approved'],
                descricao=data['description'],
                qr_code=data['point_of_interaction']['transaction_data']['qr_code'],
                qr_code64=data['point_of_interaction']['transaction_data']['qr_code_base64'],
                url=data['point_of_interaction']['transaction_data']['ticket_url'])
            if cob:
                cob.save()
                pagamento = Pagamento.objects.get(id=cob.pk)
                if pagamento:
                    context = {
                        'pagamento': pagamento,
                        'usuario': self.request.user,
                        'cpf': self.request.POST.get('cpf').replace('.', '').replace('-', '')
                    }
                    pagamento.save()
                    return render(request, 'pagamento/sucesso.html', context=context)

            return render(request, 'pagamento/erro.html', )
        else:
            return render(request, 'pagamento/erro.html', )


# ORIGIANL
# @method_decorator(csrf_exempt, name='dispatch')
# class WebHookView(View):
#     # @method_decorator(csrf_exempt, name='dispatch')
#     # def dispatch(self, request, *args, **kwargs):
#     #     return super(WebHookView, self).dispatch(request, *args, **kwargs)  # for python 2
#     #     return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         payload = self.request
#         if (payload):
#             print(request.POST.get('teste'))
#             return HttpResponse(status=200)
#         return HttpResponse(status=400)


@method_decorator(csrf_exempt, name='dispatch')
class WebHookView(View):

    def post(self, request, *args, **kwargs):
        body = json.loads(self.request.body.decode())

        mensagem = str(body)
        teste = Teste(mensagem=mensagem)
        teste.save()

        mercado_page_test = MercadoPago(
            action=body['action'],
            api_version=body['api_version'],
            application_id=body['application_id'],
            date_created=body['date_created'],
            id_web=body['id'],
            live_mode=body['live_mode'],
            type=body['type'],
            user_id=str(body['user_id']),
            data='123'
        )
        mercado_page_test.save()

        return HttpResponse(status=200)

    # def get(self):
    #     body = json.loads(self.request.body.decode())
    #     url = body['resource']
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         # Converte os dados da resposta em JSON
    #         data = response.json()
    #         mercado = MercadoPago.objects.get(id_web=str(data['collection']['id']))
    #     return HttpResponse(status=200)


class TesteView(View):
    def get(self, request, *args, **kwargs):
        url = 'https://jsonplaceholder.typicode.com/users/1'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Converte os dados da resposta em JSON
                data = response.json()
                print(data)
                context = {
                    'teste': data['name']
                }
                return render(request, 'pagamento/teste.html', context=context)
        except requests.exceptions.RequestException as e:
            ccontext = {
                'nome': e
            }
            return render(request, 'pagamento/erro.html', context=ccontext)


def lerWebook(url):
    headers = {
        'Authorization': 'Bearer APP_USR-7893702088637531-012618-cd9f06ef47c005273a3cd983a2ce2902-119438936'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            body = response.json()
            pagamento = Pagamento.objects.get(pagamento_id=body['collection']['id'])
            pagamento.status = body['collection']['status']
            pagamento.status_detalhe = body['collection']['status_detail']
            if body['collection']['status'] == 'approved':
                pagamento.usuario.atualizar_vencimento()
            pagamento.save()
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return True


@method_decorator(csrf_exempt, name='dispatch')
class WebHook(View):

    def post(self, request, *args, **kwargs):
        body = json.loads(self.request.body.decode())
        mensagem = str(body['resource'])

        pagamento = lerWebook(body['resource'])

        cobranca_id = str(body['resource']).replace('https://api.mercadolibre.com/collections/notifications/', '')

        if pagamento:
            cobranca = Cobranca(id_web=cobranca_id, mensagem='Cobrada com sucesso')
            cobranca.save()
        else:
            cobranca = Cobranca(id_web=cobranca_id, mensagem='Erro ao processar cobrança')
            cobranca.save()

        return HttpResponse(status=200)
