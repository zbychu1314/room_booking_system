# Generated by Django 5.0 on 2023-12-07 13:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sala",
            name="dostepne_wydarzenie",
        ),
    ]
