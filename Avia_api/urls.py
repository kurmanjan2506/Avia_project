from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from tickets.views import TicketViewSet, CompanyViewSet
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Avia api test project",
      default_version='v1',
      description="Test REST API backend at django",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
router = SimpleRouter()
router.register('tickets', TicketViewSet)
router.register('companies', CompanyViewSet)


urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/orders/', include('buy_tickets.urls')),
    path('api/v1/', include(router.urls)),
    path('auth/', auth),
    path('chat/', include('chat.urls')),
]

