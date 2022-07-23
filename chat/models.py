from django.db import models
from datetime import datetime


class Room(models.Model):

    title = models.CharField(max_length=1000)

class Message(models.Model):

#   room = models.ForeignKey(Room, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
# Create your models here.
