# Generated by Django 5.0.6 on 2024-06-17 21:44

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_contraloria', '0002_remove_auditoria_id_auditor_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizacion_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion_contraloria.organizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime(2024, 6, 17, 21, 44, 28, 492133))),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('estado', models.CharField(max_length=20)),
                ('organizacion_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion_contraloria.organizacion')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('reporte_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion_contraloria.reporte')),
            ],
        ),
    ]
