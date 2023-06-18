import os
from django.http import HttpResponse
from django.views.generic import TemplateView

from projeto import settings


class IndexView(TemplateView):
    template_name = 'core/index.html'


class PainelView(TemplateView):
    template_name = 'core/painel.html'


def robots(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT, 'robots.txt')
    else:
        path = os.path.join(settings.BASE_DIR, 'statics/robots.txt')
    with open(path, 'r') as arq:
        return HttpResponse(arq, content_type="text/plain")
