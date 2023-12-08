from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import WydarzenieForm
from django.contrib import messages
import datetime

# Create your views here.


def add(request):
    if not request.user.is_authenticated:
        return HttpResponse("Zaloguj sie by dodac post")
    d = datetime.datetime.now()
    d2 = datetime.datetime.now() + datetime.timedelta(hours=1)
    form = WydarzenieForm(
        initial={
            "data_rozpoczecia": d.strftime("%Y-%m-%d %H:%M:%S"),
            "data_zakonczenia": (d2.strftime("%Y-%m-%d %H:%M:%S")),
        }
    )

    if request.method == "POST":
        print(request.POST)
        form = WydarzenieForm(data=request.POST)
        print(form.as_p)
        if form.is_valid():
            wydarzenie = form.save(commit=False)
            wydarzenie.save()
            messages.add_message(request, messages.INFO, "Wydarzenie utworzone")

        return redirect("events:add")

    return render(request, "events/add.html", {"form": form})
