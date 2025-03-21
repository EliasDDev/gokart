# tokens.py
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class BookingCancellationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, booking, timestamp):
        # Using str() directly instead of six
        return str(booking.id) + str(booking.customer.id) + str(timestamp)

# Create an instance of the token generator
booking_cancellation_token = BookingCancellationTokenGenerator()
