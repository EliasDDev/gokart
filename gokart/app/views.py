from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Booking
import json
from datetime import time

# Create your views here.

def home(request):
    return render(request, "index.html")

def get_available_slots(request):
    date = request.GET.get("date")

    # Define possible time slots
    all_slots = [time(10, 00), time(10, 30), time(13, 0), time(14, 0)]

    # Get already booked slots for the selected date
    booked_slots = Booking.objects.filter(date=date).values_list("time", flat=True)

    # Filter out booked slots
    available_slots = [slot.strftime("%H:%M") for slot in all_slots if slot not in booked_slots]

    print(booked_slots)
    return JsonResponse({"slots": available_slots})

def book_slot(request):
    if request.method == "POST":
        #data = json.loads(request.body)

        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        time =request.POST.get("time")

        # Check if the slot is available
        if Booking.objects.filter(date=date, time=time).exists():
            return JsonResponse({"error": "Slot already booked"}, status=400)

        # Save the booking
        Booking.objects.create(name = name, email = email, date = date, time = time)
        return JsonResponse({"success": "Booking confirmed"})