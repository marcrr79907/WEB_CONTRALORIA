# Generated by Django 4.1.7 on 2024-06-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_contraloria', '0004_alter_organizacion_en_supervision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporte',
            old_name='costos_de_ersonal',
            new_name='costos_de_personal',
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]