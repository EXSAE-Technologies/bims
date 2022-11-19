from django.db import models

# Create your models here.
class Ticket(models.Model):
    wager=models.FloatField()

    def bet_type(self)->str:
        betType=""
        if len(self.bets.all()) > 1:
            betType = "Multiple Bets"
        elif len(self.bets.all()) == 1:
            betType = "Single Bets"
        return betType
    
    def odds(self)->float:
        totalOdds = 0.0
        for bet in self.bets.all():
            totalOdds += bet.odds
        return totalOdds
    
    def profit(self)->float:
        return self.odds()*self.wager

class Bet(models.Model):
    ticket=models.ForeignKey(Ticket,related_name="bets",on_delete=models.CASCADE)
    matchid=models.IntegerField()
    name=models.CharField(max_length=200)
    odds=models.FloatField()

    def __str__(self) -> str:
        return f"Match:{self.matchid} -> {self.name} -> {self.odds}"