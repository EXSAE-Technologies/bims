from django.contrib import admin
from tickets.models import Ticket, Bet
# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=["id","bet_type","odds","wager","profit"]

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display=["ticket","matchid","name"]