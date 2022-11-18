from django.urls import path
from tickets.rest.views import TicketView, TicketDetail

app_name="ticket-api"
urlpatterns=[
    path('',TicketView.as_view(),name="tickets"),
    path('id/<pk>',TicketDetail.as_view(),name="ticket-detail")
]