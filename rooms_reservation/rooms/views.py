from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sala

from django.contrib import messages

# adres -> funkcja -> szablon
# posts -> list -> posts/list.html


def list(request):
    rooms = Sala.objects.all()
    return render(request, "rooms/list.html", {"rooms": rooms})


def details(request, id):
    if request.method == "POST":
        Sala.objects.create(
            content=request.POST.get("nazwa"),
        )

    return render(request, "rooms/details.html", {"room": Sala.objects.get(id=id)})
