from django.contrib.auth.tokens import PasswordResetTokenGenerator


# Generate password to prevent unauthorized people to cancel others bookings
class BookingCancellationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, booking, timestamp):
        return str(booking.id) + str(booking.customer.id) + str(timestamp)


# Create an instance of the token generator
booking_cancellation_token = BookingCancellationTokenGenerator()
