from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Sala(models.Model):
    nazwa = models.CharField(max_length=255)
    lokalizacja = models.CharField(max_length=255)
    pojemnosc = models.IntegerField()
    dostepne_wyposazenie = models.CharField(max_length=255)
    zdjecie = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nazwa