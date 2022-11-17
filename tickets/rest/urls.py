from django.urls import path
from tickets.rest.views import TicketView

app_name="ticket-api"
urlpatterns=[
    path('',TicketView.as_view(),name="tickets"),
]