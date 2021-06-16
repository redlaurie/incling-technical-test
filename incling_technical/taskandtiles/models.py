from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Tile(models.Model):
    date_posted = models.DateTimeField()
    status_choices = (('Live', 'Live'),('Pending', 'Pending'), ('Archived','Archived'),)
    status = models.CharField(max_length = 100, choices = status_choices, default="Live")

class Task(models.Model):
    title = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True,null=True)
    description = models.TextField()
    type_choices = (('survey', 'survey'),('discussion', 'discussion'), ('diary','diary'),)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, blank=True,null=True)