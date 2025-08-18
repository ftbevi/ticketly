from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from apps.accounts.urls import urlpatterns
from apps.servicedesk.urls import urlpatterns as ticket_url


admin.site.site_header = "Ticketly"
admin.site.site_title = "Ticketly"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urlpatterns)),
    path('tickets/', include(ticket_url)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
