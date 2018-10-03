from django.contrib import admin

from Inventarios.models import Medida
from Inventarios.models import Insumo
from Inventarios.models import InsumoCategoria
from Compras.models import InsumoProveedor


class MedidaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

admin.site.register(Medida,MedidaAdmin)

class InsumoProveedorTabularInline(admin.TabularInline):
	model = InsumoProveedor

class InsumoAdmin(admin.ModelAdmin):
	inlines = [InsumoProveedorTabularInline,]
	filter_horizontal = ('insumoCategoria',)
	list_instances = True	
	class Meta:
		model = Insumo

admin.site.register(Insumo,InsumoAdmin)
admin.site.register(InsumoCategoria)