from __future__ import unicode_literals

from django.db import models

class EmpleadoCargo(models.Model):
    class Meta:
        verbose_name_plural = 'empleado cargo'
    nombre = models.CharField(max_length=32)
    description = models.TextField(max_length=232)
    #cargoEmpleadoBajoMando = models.ManyToManyField(CargoEmpleado, blank=True, null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre

class Organigrama(models.Model):
    class Meta:
        verbose_name_plural = 'organigrama'
    cargo = models.OneToOneField(EmpleadoCargo, on_delete=models.CASCADE, related_name="cargoMando")
    cargoSuperior = models.ForeignKey(EmpleadoCargo, on_delete=models.CASCADE, related_name="empleadoCargo", blank=True, null=True)
    cargosBajoMando = models.ManyToManyField(EmpleadoCargo)
    description = models.TextField(max_length=232)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.cargo.nombre

class Empleado(models.Model):
    codigo = models.AutoField(primary_key=True)
    activo = models.BooleanField(default=True)
    cedula = models.CharField(max_length=22,blank=True)
    nombre = models.CharField(max_length=32)
    cargos = models.ManyToManyField(EmpleadoCargo)
    salario = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    direccion = models.CharField(max_length=32,blank=True)
    telefonos = models.CharField(max_length=100)
    email = models.EmailField(max_length=32,blank=True)
    descripcion = models.TextField(max_length=232,blank=True)    
    fechaIngreso = models.DateTimeField(auto_now_add=True,blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre

class Contratacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    activo = models.BooleanField(default=True)
    nitoCedula = models.CharField(max_length=22,blank=True)
    nombre = models.CharField(max_length=32)
    cargos = models.ForeignKey(EmpleadoCargo, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=32,blank=True)
    telefonos = models.CharField(max_length=100)
    email = models.EmailField(max_length=32,blank=True)
    descripcion = models.TextField(max_length=232,blank=True)    
    fechaIngreso = models.DateTimeField(auto_now_add=True,blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre