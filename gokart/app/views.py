from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .models import Customer, Gokart, Booking, Drivers
from datetime import time
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.

def home(request):
    return render(request, "index.html")

def success(request):
    return render(request, "success.html")

def failed(request):
    return render(request, "failed.html")

def data(request):
    bookings = Booking.objects.prefetch_related('drivers_set__gokart').all().order_by('date', 'time')
    return render(request, 'data.html', {'bookings': bookings})

def get_available_slots(request):
    date = request.GET.get("date")

    # Define possible time slots
    all_slots = [time(10, 00), time(10, 30),
                 time(11, 00), time(11, 30),
                 time(13, 00), time(13, 30),
                 time(14, 00), time(14, 30)]

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

        if time is None or time == 0 or time == "":
            messages.error(request, "Ingen vald tid hittad för bokningen. Vänligen försök igen.")
            return redirect("failed")

        # Check if the slot is available
        if Booking.objects.filter(date=date, time=time).exists():
            messages.error(request, "Tiden du angav är tyvärr redan uppbokad, vänligen försök igen med en annan tid.")
            return redirect("failed")
            #return JsonResponse({"error": "Slot already booked"}, status=400)

        customer, created = Customer.objects.get_or_create(email=email, defaults={'name': name})

        # Create a new booking instance, but don't save it yet
        booking = Booking.objects.create(date=date, time=time, customer=customer)

        # Loop through the number of people and add the selected gokarts to the booking
        for i in range(1, num_people + 1):
            gokart_id = request.POST.get(f"gokart_id_{i}")
            gokart = Gokart.objects.get(id=gokart_id)
            Drivers.objects.create(gokart=gokart, booking=booking)

        send_booking_confirmation_mail(name, email, date, time)

        return redirect("success")
        #return JsonResponse({"success": "Booking confirmed"})

def cancel_booking(request):
    if request.method == "POST":
        booking_id = request.POST.get("booking_id")
        booking = get_object_or_404(Booking, id=booking_id)
        customer = booking.customer

        booking.delete()

        if not Booking.objects.filter(customer=customer).exists():
            customer.delete()

        return redirect("data")

    return HttpResponse("Invalid request", status=400)

# We are using https://app.mailersend.com as our SMTP host provider.
def send_booking_confirmation_mail(name, mail, date, time):
    # Email details
    sender_email = "MS_62DvdC@trial-yzkq340vvvkld796.mlsender.net"
    receiver_email = mail
    password = "mssp.PyDKoSt.7dnvo4deo3rl5r86.NHJoMli"
    subject = "Gokart booking confirmation"
    body = f"Hello {name},\nWe have received a gokart booking for you on the {date} at {time}.\nHope to see you there.\nWould you like to cancel your booking?\nLink: TODO"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Set up the SMTP server
    smtp_server = "smtp.mailersend.net"
    port = 587

    # Send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
