from django import forms
from .models import Rezerwacja
import sys
sys.path.append("..")
from events.models import Wydarzenie
from rooms.models import Sala



class SelectForManyToMany(forms.Select):

    def value_from_datadict(self, data, files, name):
        try:
            getter = data.getlist
        except AttributeError:
            getter = data.get
        return getter(name)

class RezerwacjaForm(forms.ModelForm):
    class Meta:
        model = Rezerwacja
        fields = ["referencja_sala","referencja_wydarzenie"]
        widgets = {'supplier': SelectForManyToMany}