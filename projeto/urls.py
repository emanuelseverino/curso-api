from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from core.views import robots, WebHookView
from usuario.api.viewsets import CustomAuthToken, ChangePasswordView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__ / ', include('debug_toolbar.urls')),
    path('', include('core.urls'), ),
    path('login/', CustomAuthToken.as_view(), ),
    path('mudar-senha/', ChangePasswordView.as_view(), ),
    path('resetar-senha/', include('django_rest_passwordreset.urls', namespace='resetar_senha')),
    path('usuario/', include('usuario.urls'), ),
    path('perfil/', include('perfil.urls'), ),
    path('contas/', include("django.contrib.auth.urls")),
    path('robots.txt', robots, ),
    path('webhook/', WebHookView.as_view(), name='webhook', ),
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa E501
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
