from django.contrib import admin
from .models import Sala

# Register your models here.
class SalaAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "lokalizacja", "pojemnosc","dostepne_wyposazenie","zdjecie"]

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

#class CategoryAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Sala, SalaAdmin)
#admin.site.register(Category, CategoryAdmin)