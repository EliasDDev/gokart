from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.EmailField()

class Gokart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default="2025-01-01")
    time = models.TimeField(default="00:00")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)

class Drivers(models.Model):
    id = models.AutoField(primary_key=True)
    gokart = models.ForeignKey(Gokart, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)