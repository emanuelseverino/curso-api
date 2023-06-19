import requests
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from hook.models import Cobranca, Pagamento, MercadoPago, Teste


class PagarView(LoginRequiredMixin, View):
    login_url = '/contas/login'

    def get(self, request, *args, **kwargs):
        return render(request, 'pagamento/pagar.html')

    def post(self, request, *args, **kwargs):
        data = {
            "transaction_amount": 1,
            "description": "Compra API",
            "payment_method_id": "pix",
            "payer": {
                "email": "emanueldesouza@hotmail.com",
                "first_name": "Emanuel",
                "last_name": "Severino",
                "identification": {
                    "type": "CPF",
                    "number": "12571773704"
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
            _cobranca = Cobranca(pagamento_id=data['id'], status=data['status'], status_detalhe=data['status_detail'],
                                 criado_em=data['date_created'], atualizado_em=data['status'],
                                 pago_em=data['date_approved'],
                                 descricao=data['description'],
                                 qr_code=data['point_of_interaction']['transaction_data']['qr_code_base64'],
                                 qr_code64=data['point_of_interaction']['transaction_data']['qr_code_base64'],
                                 url=data['point_of_interaction']['transaction_data']['ticket_url'])

            if _cobranca:
                _cobranca.save()
                obj_cobranca = Cobranca.objects.get(id=_cobranca.pk)
                pagamento = Pagamento(usuario=self.request.user, pagamento=obj_cobranca, status=_cobranca.status)
                if pagamento:
                    context = {
                        'pagamento': pagamento.pagamento
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
        Teste.create(mensagem=self.request.str)
        payload = self.request.get_json()
        converted_data = {}
        for key, value in payload.items():
            converted_data[key] = str(value)
        if (payload):
            mercado_page = MercadoPago.objects.create(**converted_data)
            mercado_page.id_web = converted_data['id']
            mercado_page.save()
            return HttpResponse(status=200)
        return HttpResponse(status=400)
