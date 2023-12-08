from django.contrib import admin
from .models import Wydarzenie

# Register your models here.
class WydarzenieAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "opis", "data_rozpoczecia","data_zakonczenia"]
    
    def short_descriptiopn(self, obj):
        return obj.dostepne_wydarzenie[:20] + "..."
    

    def get_list_display(self, request):
        """
        Return a sequence containing the fields to be displayed on the
        changelist.
        """
        if request.user.is_superuser is False:
            return ["nazwa"]
        return self.list_display

admin.site.register(Wydarzenie, WydarzenieAdmin)