from django.contrib import admin
from tickets.models import Ticket, Bet
# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display=["ticket","matchid","name"]