from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Rezerwacja
from .forms import RezerwacjaForm
from django.contrib import messages
from datetimerange import DateTimeRange

# Create your views here.


def list_reservations(request):
    rezerwacje_ref_sala, rezerwacje = prepare_rez_objects()
    lista_rezerwacji = zip(rezerwacje_ref_sala, rezerwacje)
    return render(request, "reservations/list.html", {"reservations": lista_rezerwacji})


def prepare_rez_objects():
    rezerwacje_ref_sala = [
        rez for rez in Rezerwacja.referencja_sala.through.objects.all()
    ]
    rezerwacje = Rezerwacja.objects.all()
    return rezerwacje_ref_sala, rezerwacje


def add_reservation(request):
    if not request.user.is_authenticated:
        return HttpResponse("Zaloguj sie by dodac post")

    form = RezerwacjaForm()
    rezerwacje_ref_sala, rezerwacje = prepare_rez_objects()
    lista_rezerwacji = zip(rezerwacje_ref_sala, rezerwacje)
    if request.method == "POST":
        form = RezerwacjaForm(data=request.POST)

        if form.is_valid():
            id = form.cleaned_data["referencja_sala"].values()[0]["id"]
            selected_start_time = form.cleaned_data[
                "referencja_wydarzenie"
            ].data_rozpoczecia
            selected_end_time = form.cleaned_data[
                "referencja_wydarzenie"
            ].data_zakonczenia
            for rez_ref_sala, rez_ref_wydarzenie in lista_rezerwacji:
                print(f"ID: {id}")
                if rez_ref_sala.sala.id == id:
                    registered_start_time = (
                        rez_ref_wydarzenie.referencja_wydarzenie.data_rozpoczecia
                    )
                    registered_end_time = (
                        rez_ref_wydarzenie.referencja_wydarzenie.data_zakonczenia
                    )
                    time_range_selected = DateTimeRange(
                        selected_start_time, selected_end_time
                    )
                    time_range_registered = DateTimeRange(
                        registered_start_time, registered_end_time
                    )
                    time_is_overlapping = time_range_registered.is_intersection(
                        time_range_selected
                    )

                    if time_is_overlapping is True:
                        messages.add_message(
                            request,
                            messages.INFO,
                            f"INFO: W wybranym czasie {selected_start_time}:{selected_end_time} sala {rez_ref_sala.sala.nazwa} jest juz zarezerwowana ",
                        )
                        return render(
                            request,
                            "reservations/add_reservation.html",
                            {
                                "form": form,
                            },
                        )

            rezerwacja = form.save()
            if rezerwacja:
                messages.add_message(
                    request,
                    messages.INFO,
                    f"INFO: Wybrana Sala zostala zarezerwowana w wybranym terminie",
                )

        else:
            print(type(form.errors))
            if "wydarzenie already exists" in form.errors.as_text():
                messages.add_message(
                    request, messages.INFO, f"INFO: Wydarzenie jest juz dodane do listy"
                )
        return redirect("reservations:list_reservations")

    return render(request, "reservations/add_reservation.html", {"form": form})
