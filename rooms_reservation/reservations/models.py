from django.db import models

# Create your models here.
class Rezerwacja(models.Model):
    referencja_sala = models.ManyToManyField('rooms.Sala',related_name="ref_sala")
    referencja_wydarzenie = models.OneToOneField('events.Wydarzenie', on_delete=models.CASCADE,related_name="ref_wydarzenie")
    