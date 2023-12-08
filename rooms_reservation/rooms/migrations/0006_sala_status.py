# Generated by Django 3.2.7 on 2023-12-07 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_remove_sala_dostepne_wydarzenie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='status',
            field=models.CharField(choices=[('1', 'dostepna'), ('2', 'zajeta')], default=1, max_length=15),
            preserve_default=False,
        ),
    ]
