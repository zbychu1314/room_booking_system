from django import forms
from .models import Wydarzenie

class WydarzenieForm(forms.ModelForm):
    class Meta:
        model = Wydarzenie
        fields = ["nazwa","opis","data_rozpoczecia","data_zakonczenia"]

