# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-09-30 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratacion',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('nitoCedula', models.CharField(blank=True, max_length=22)),
                ('nombre', models.CharField(max_length=32)),
                ('direccion', models.CharField(blank=True, max_length=32)),
                ('telefonos', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=32)),
                ('descripcion', models.TextField(blank=True, max_length=232)),
                ('fechaIngreso', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('cedula', models.CharField(blank=True, max_length=22)),
                ('nombre', models.CharField(max_length=32)),
                ('salario', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('direccion', models.CharField(blank=True, max_length=32)),
                ('telefonos', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=32)),
                ('descripcion', models.TextField(blank=True, max_length=232)),
                ('fechaIngreso', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoCargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=232)),
            ],
            options={
                'verbose_name_plural': 'empleado cargo',
            },
        ),
        migrations.CreateModel(
            name='Organigrama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=232)),
                ('cargo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cargoMando', to='RRHH.EmpleadoCargo')),
                ('cargoSuperior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleadoCargo', to='RRHH.EmpleadoCargo')),
                ('cargosBajoMando', models.ManyToManyField(to='RRHH.EmpleadoCargo')),
            ],
            options={
                'verbose_name_plural': 'organigrama',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='cargos',
            field=models.ManyToManyField(to='RRHH.EmpleadoCargo'),
        ),
        migrations.AddField(
            model_name='contratacion',
            name='cargos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RRHH.EmpleadoCargo'),
        ),
    ]
