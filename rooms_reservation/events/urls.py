from django.urls import path
from . import views

app_name = "events" 
urlpatterns = [
    #path("rooms/", views.list, name="list"),
    #path("rooms/<int:id>/", views.details, name="details"),
    path("events/add/", views.add, name="add"),
  
]