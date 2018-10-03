# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-02 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0002_auto_20181002_0149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insumoproveedor',
            old_name='descripcion',
            new_name='observacion',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='Pais',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='Region',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='ciudad',
            field=models.CharField(blank=True, max_length=42),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, max_length=52),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=42),
        ),
    ]