# Generated by Django 3.2.7 on 2023-12-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20231207_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wydarzenie',
            name='opis',
            field=models.TextField(),
        ),
    ]
