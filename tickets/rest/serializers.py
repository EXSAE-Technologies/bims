from rest_framework import serializers
from tickets.models import Ticket, Bet

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bet
        fields="__all__"

class TicketSerializer(serializers.ModelSerializer):
    bets=BetSerializer(many=True)

    class Meta:
        model=Ticket
        fields="__all__"

    def create(self, validated_data):
        bets_data = validated_data.pop("bets")
        ticket = Ticket.objects.create(**validated_data)
        for bet_data in bets_data:
            Bet.objects.create(ticket=ticket,**bet_data)
        return ticket
