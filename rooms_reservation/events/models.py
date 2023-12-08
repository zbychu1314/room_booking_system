from django.db import models

# Create your models here.

class Wydarzenie(models.Model):
    nazwa = models.CharField(max_length=255)
    opis = models.TextField()
    data_rozpoczecia = models.DateTimeField(editable=True)
    data_zakonczenia = models.DateTimeField(editable=True)
    #autor = models.ForeignKey("auth.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa