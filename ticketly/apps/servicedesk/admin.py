from django.contrib import admin

from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "priority", "sector", "status")
    fields = ("title", "priority", "sector", "status")
