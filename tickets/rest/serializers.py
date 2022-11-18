from rest_framework import serializers
from tickets.models import Ticket, Bet

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bet
        fields="__all__"

class TicketSerializer(serializers.ModelSerializer):
    bets=BetSerializer(many=True,read_only=True)

    class Meta:
        model=Ticket
        fields="__all__"
