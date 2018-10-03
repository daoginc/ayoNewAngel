from django.contrib import admin

from Ventas.models import Cliente
from Ventas.models import ClienteTipo
from Ventas.models import FormaContacto

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre','fechaIngreso','puntos')
	filter_horizontal = ('formaContacto',)
	list_instances = True
	search_fields = ['codigo','nombre']

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(ClienteTipo)
admin.site.register(FormaContacto)