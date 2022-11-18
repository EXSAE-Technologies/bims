from rest_framework.views import APIView
from rest_framework.response import Response
from tickets.rest import serializers
from tickets.models import Ticket, Bet

class TicketView(APIView):

    def get(self,request):
        tickets=Ticket.objects.all()
        ticketsData = serializers.TicketSerializer(tickets,many=True)
        return Response(ticketsData.data)

    def post(self,request):
        ticket = serializers.TicketSerializer(data=request.data)

        res = dict()
        if ticket.is_valid():
            ticket.save()
            for bet in request.data["bets"]:
                betObject = Bet.objects.create(ticket=ticket.instance,**bet)
                betObject.save()
            res["success"]=True
        else:
            res["success"]=False
        res["data"]=ticket.data
        
        return Response(res)

class TicketDetail(APIView):
    def get(self,request,pk):
        ticket=Ticket.objects.get(pk=pk)
        ticketData=serializers.TicketSerializer(ticket)
        return Response(ticketData.data)