from django.contrib import admin
from django.urls import path, include

from apps.accounts.urls import urlpatterns

admin.site.site_header = "Ticketly"
admin.site.site_title = "Ticketly"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urlpatterns)),
]
