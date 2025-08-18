from rest_framework.routers import DefaultRouter

from apps.servicedesk.views.api import ticket

router = DefaultRouter()
router.register(r"", ticket.TicketViewSet, basename="ticket")

urlpatterns = router.urls