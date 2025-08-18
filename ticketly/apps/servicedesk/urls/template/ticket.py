from django.urls import path

from apps.servicedesk.views.template.ticket_list import TicketListPageView

urlpatterns = [
    path('', TicketListPageView.as_view(), name='ticket_list')
]
