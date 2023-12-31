# Generated by Django 3.2.7 on 2023-12-07 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_remove_sala_status'),
        ('events', '0004_alter_wydarzenie_opis'),
        ('reservations', '0002_auto_20231207_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezerwacja',
            name='czas_rozpoczecia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ref_czas_rozpoczecia', to='events.wydarzenie'),
        ),
        migrations.AlterField(
            model_name='rezerwacja',
            name='czas_zakonczenia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ref_czas_zakonczenia', to='events.wydarzenie'),
        ),
        migrations.AlterField(
            model_name='rezerwacja',
            name='referencja_sala',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ref_sala', to='rooms.sala'),
        ),
        migrations.AlterField(
            model_name='rezerwacja',
            name='referencja_wydarzenie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ref_wydarzenie', to='events.wydarzenie'),
        ),
    ]
