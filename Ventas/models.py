from __future__ import unicode_literals

from django.db import models

class ClienteTipo(models.Model):
    class Meta:
        verbose_name_plural = 'cliente tipo'
    nombre = models.CharField(max_length=32)
    description = models.TextField(max_length=232)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre
class FormaContacto(models.Model):
    class Meta:
        verbose_name_plural = 'Forma contacto'
    nombre = models.CharField(max_length=140,null=False)
    descripcion=models.TextField(max_length=232,null=True,blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre
class Cliente(models.Model): #pais, departamento, ciudad, forma de contacto, referido en la vista anexar el id y posibilidad de busqueda por campo
    codigo = models.AutoField(primary_key=True)
    activo = models.BooleanField(default=True)
    nombre = models.CharField(max_length=32)
    Pais = models.CharField(max_length=42,blank=True)
    Region = models.CharField(max_length=42,blank=True)
    ciudad = models.CharField(max_length=42,blank=True)
    direccion = models.CharField(max_length=52,blank=True)
    telefonos = models.CharField(max_length=100)
    email = models.EmailField(max_length=32,blank=True)
    descripcion = models.TextField(max_length=232,blank=True)    
    fechaIngreso = models.DateTimeField(auto_now_add=True,blank=True)
    fechaNacimiento = models.DateField(null=True,blank=True)
    puntos = models.PositiveSmallIntegerField(null=True,blank=True)
    #codigoReferido = 
    clienteTipo= models.ForeignKey(ClienteTipo, on_delete=models.CASCADE)
    formaContacto = models.ManyToManyField(FormaContacto, verbose_name="formaContacto")

    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre
