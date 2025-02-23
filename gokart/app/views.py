from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Customer, Gokart, Booking, Drivers
from datetime import time

# Create your views here.

def home(request):
    return render(request, "index.html")

def data(request):
    bookings = Booking.objects.prefetch_related('drivers_set__gokart').all().order_by('date', 'time')
    return render(request, 'data.html', {'bookings': bookings})

def get_available_slots(request):
    date = request.GET.get("date")

    # Define possible time slots
    all_slots = [time(10, 00), time(11, 00), time(13, 00), time(14, 00)]

    # Get already booked slots for the selected date
    booked_slots = Booking.objects.filter(date=date).values_list("time", flat=True)

    # Filter out booked slots
    available_slots = [slot.strftime("%H:%M") for slot in all_slots if slot not in booked_slots]

    return JsonResponse({"slots": available_slots})

def get_gokarts(request):
    gokarts = Gokart.objects.all()
    gokart_list = [{"id": gokart.id, "name": gokart.name} for gokart in gokarts]
    return JsonResponse(gokart_list, safe=False)

def book_slot(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        time = request.POST.get("time")
        num_people = int(request.POST.get("num_people"))  # Number of people

        # Check if the slot is available
        if Booking.objects.filter(date=date, time=time).exists():
            return JsonResponse({"error": "Slot already booked"}, status=400)

        customer, created = Customer.objects.get_or_create(email=email, defaults={'name': name})

        # Create a new booking instance, but don't save it yet
        booking = Booking.objects.create(date=date, time=time, customer=customer)

        # Loop through the number of people and add the selected gokarts to the booking
        for i in range(1, num_people + 1):
            gokart_id = request.POST.get(f"gokart_id_{i}")
            gokart = Gokart.objects.get(id=gokart_id)
            Drivers.objects.create(gokart=gokart, booking=booking)

        return JsonResponse({"success": "Booking confirmed"})