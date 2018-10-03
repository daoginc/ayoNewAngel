from __future__ import unicode_literals

from django.db import models
from Inventarios.models import Insumo
from Inventarios.models import InsumoCategoria

class Proveedor(models.Model): #pais, departamento, ciudad, forma de contacto, referido en la vista anexar el id y posibilidad de busqueda por campo
    codigo = models.AutoField(primary_key=True)
    activo = models.BooleanField(default=True)
    nitoCedula = models.CharField(max_length=22,blank=True)
    nombre = models.CharField(max_length=42)
    Pais= models.CharField(max_length=42,blank=True)
    Region = models.CharField(max_length=42,blank=True)
    ciudad = models.CharField(max_length=42,blank=True)
    direccion = models.CharField(max_length=52,blank=True)
    telefonos = models.CharField(max_length=100)
    email = models.EmailField(max_length=32,blank=True)
    descripcion = models.TextField(max_length=232,blank=True)    
    fechaIngreso = models.DateTimeField(auto_now_add=True,blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre

class ProveedorCuenta(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fechaIngreso = models.DateField(auto_now_add=True)
    banco = models.CharField(max_length=43)
    TIPO_CHOICES = (('ahorro', 'AHORRO',), ('corriente', 'CORRIENTE',))
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, null=False)
    cuenta = models.BigIntegerField(null=False,blank=False)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.proveedor.nombre


class ProveedorContacto(models.Model): #pais, departamento, ciudad, forma de contacto, referido en la vista anexar el id y posibilidad de busqueda por campo
    codigo = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=32)
    cargo = models.CharField(max_length=10, null=True, blank=True)
    telefonos=models.CharField(max_length=100, blank=True)
    email=models.EmailField(max_length=32, blank=True)
    fechaIngreso=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.proveedor.nombre


class InsumoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=43)
    precio = models.DecimalField(max_digits=12, decimal_places=2,verbose_name="precio")
    observacion = models.TextField(max_length=232, null=True, blank = True)
    insumoCategoria = models.ManyToManyField(InsumoCategoria, verbose_name="InsumoCategoria")
    cantidadAlmacen = models.DecimalField(max_digits=12, decimal_places=2,verbose_name="cantidadAlmacen")
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.proveedor.nombre
