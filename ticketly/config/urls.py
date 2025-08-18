from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps.accounts.urls.template import auth as template_auth
from apps.accounts.urls.api import auth
from apps.servicedesk.urls.template import ticket as template_ticket
from apps.servicedesk.urls.api import ticket


admin.site.site_header = "Ticketly"
admin.site.site_title = "Ticketly"

urlpatterns = [
    path('admin/', admin.site.urls),
    # template views
    path('accounts/', include(template_auth.urlpatterns)),
    path('tickets/', include(template_ticket.urlpatterns)),
    # api views
    path("api/auth/", include(auth.urlpatterns)),
    path("api/tickets/", include(ticket.urlpatterns)),
    # docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(), name="redoc"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
