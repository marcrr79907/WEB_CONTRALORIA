# Generated by Django 4.1.7 on 2024-06-27 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_contraloria', '0005_rename_costos_de_ersonal_reporte_costos_de_personal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 6, 27, 6, 34, 9, 657854)),
        ),
    ]