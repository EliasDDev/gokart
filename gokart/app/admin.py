from django.contrib import admin
from .models import Customer, Gokart, Booking, Drivers

# Register your models here.

admin.site.register(Customer)
admin.site.register(Gokart)
admin.site.register(Booking)
admin.site.register(Drivers)