from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100, null=True, blank=True)


class Activity(models.Model):
    username = models.CharField(max_length=150)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.username} - {self.type}"


class Workout(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.username} - {self.name}"


class Leaderboard(models.Model):
    team_name = models.CharField(max_length=100)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.team_name} - {self.score}"
