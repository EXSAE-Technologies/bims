from rest_framework.views import APIView
from rest_framework.response import Response
from tickets.rest import serializers
from tickets.models import Ticket

class TicketView(APIView):

    def get(self,request):
        tickets=Ticket.objects.all()
        ticketsData = serializers.TicketSerializer(tickets,many=True)
        return Response(ticketsData.data)

    def post(self,request):
        ticket = serializers.TicketSerializer(request.data)
        ticket.save()
        return Response(ticket.data)
