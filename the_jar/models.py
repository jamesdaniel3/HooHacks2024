from django.db import models
from django.contrib.auth.models import User

class Jar(models.Model):
    class ModeChoices(models.TextChoices):
        OPTION_ONE = 'Option One', 'Option One Description'
        OPTION_TWO = 'Option Two', 'Option Two Description'
        OPTION_THREE = 'Option Three', 'Option Three Description'

    name = models.CharField(max_length=100)
    users_in_jar = models.ManyToManyField(User)
    mode = models.CharField(max_length=20, choices=ModeChoices.choices)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    reward = models.CharField(max_length=100, null=True, blank=True)
    punishment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name