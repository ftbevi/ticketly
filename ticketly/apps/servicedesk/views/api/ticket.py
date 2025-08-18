from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.servicedesk.serializers import TicketSerializer
from apps.servicedesk.models import Ticket


@extend_schema(tags=["Tickets"])
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
