# Generated by Django 4.1.7 on 2024-06-28 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_contraloria', '0009_remove_reporte_condiciones_económicas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporte',
            name='necesidades_tecnológicas',
        ),
        migrations.RemoveField(
            model_name='reporte',
            name='reservas_de_contingencia',
        ),
    ]
