from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehicle (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    amount = models.IntegerField()
    description = models.TextField()
    image_link = models.TextField(default="", blank=True)
    