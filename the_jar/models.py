from django.db import models
from django.contrib.auth.models import User


class Jar(models.Model):
    class ModeChoices(models.TextChoices):
        LAST_MAN = "Last Jarling Standing", "Last Jarling standing wins"
        COUNT = "Count", "The Jarling with the most Jams at the end of the competition wins"
        BATTLE_ROYALE = "Battle Royale", ("On every interval, the Jarling with the least Jams dropped will fall out "
                                          "of the competition till one remains")

    name = models.CharField(max_length=100)
    users_in_jar = models.ManyToManyField(User)
    mode = models.CharField(max_length=900, choices=ModeChoices.choices)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    reward = models.CharField(max_length=100, null=True, blank=True)
    punishment = models.CharField(max_length=100, null=True, blank=True)


class Jam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jar = models.ForeignKey(Jar, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(auto_now_add=True)

