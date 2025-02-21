from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    date = models.DateField(default="2025-01-01")
    time = models.TimeField(default="00:00")