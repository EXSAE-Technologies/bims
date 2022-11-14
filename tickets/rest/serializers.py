from rest_framework.serializers import ModelSerializer
from tickets.models import Ticket, Bet

class TicketSerializer(ModelSerializer):
    class Meta:
        model=Ticket
        fields="__all__"

class BetSerializer(ModelSerializer):
    class Meta:
        model=Bet
        fields="__all__"