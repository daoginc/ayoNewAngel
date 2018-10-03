from __future__ import unicode_literals

from django.db import models

class Medida(models.Model):
    nombre = models.CharField(max_length=43)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre
        
class InsumoCategoria(models.Model):
    class Meta:
        verbose_name_plural = 'InsumoCategoria'
    nombre = models.CharField(max_length=32)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre


class Insumo(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(max_length=43)
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=232, null=False)
    insumoCategoria = models.ManyToManyField(InsumoCategoria, verbose_name="InsumoCategoria")
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre


