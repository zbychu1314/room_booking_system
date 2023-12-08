from django.urls import path
from . import views

app_name = "rooms" 
urlpatterns = [
    path("rooms/", views.list, name="list"),
    path("rooms/<int:id>/", views.details, name="details"),
    #path("rooms/add/", views.add, name="add"),
  
]
