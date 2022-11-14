from django.db import models

# Create your models here.
class Ticket(models.Model):
    wager=models.FloatField()

class Bet(models.Model):
    ticket=models.ForeignKey(Ticket,related_name="bets",on_delete=models.CASCADE)
    matchid=models.IntegerField()
    name=models.CharField(max_length=200)
    odds=models.FloatField()

    def __str__(self) -> str:
        return f"Match:{self.matchid} -> {self.name} -> {self.odds}"