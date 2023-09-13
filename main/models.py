from django.db import models

# Create your models here.
class Vehicle (models.Model):
    name = models.CharField(max_length=20)
    amount = models.IntegerField()
    description = models.TextField()
    image_link = models.TextField(default="", blank=True)