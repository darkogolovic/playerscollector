from django.db import models
from django.contrib.auth.models import User




class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Coach(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   
    coaches = models.ManyToManyField(Coach, blank=True)

    def __str__(self):
        return self.name

