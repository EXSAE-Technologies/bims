from rest_framework.routers import SimpleRouter
from tickets.rest.views import TicketView

router = SimpleRouter()
router.register(r"tickets",TicketView.as_view(),basename="tickets")