# Generated by Django 4.1.3 on 2022-11-14 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wager', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchid', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('odds', models.FloatField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bets', to='tickets.ticket')),
            ],
        ),
    ]
