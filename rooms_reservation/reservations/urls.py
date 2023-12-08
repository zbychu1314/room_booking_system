from django.urls import path
from . import views

app_name = "reservations" 
urlpatterns = [
    path("reservations/", views.list_reservations, name="list_reservations"),
    #path("rooms/<int:id>/", views.details, name="details"),
    path("reservations/add_reservation/", views.add_reservation, name="add_reservation"),
  
]