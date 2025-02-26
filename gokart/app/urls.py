from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("success", views.success, name="success"),
    path("failed", views.failed, name="failed"),
    path("data", views.data, name="data"),
    path("get-available-slots/", views.get_available_slots, name="get_available_slots"),
    path('get-gokarts/', views.get_gokarts, name='get_gokarts'),
    path("book-slot/", views.book_slot, name="book_slot"),
    path("cancel-booking/", views.cancel_booking, name="cancel_booking"),
]