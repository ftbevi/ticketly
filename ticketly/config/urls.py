from django.contrib import admin
from django.urls import path

admin.site.site_header = "Ticketly"
admin.site.site_title = "Ticketly"

urlpatterns = [
    path('admin/', admin.site.urls),
]
