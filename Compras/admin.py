from django.contrib import admin

from Compras.models import Proveedor
from Compras.models import ProveedorContacto
from Compras.models import ProveedorCuenta

from Compras.models import InsumoProveedor

class ProveedorContactoAdmin(admin.ModelAdmin):
	list_display = ('nombre','cargo','email','telefonos')

class ProveedorContactoTabularInline(admin.TabularInline):
	model = ProveedorContacto

class ProveedorCuentaAdmin(admin.ModelAdmin):
	list_display = ('proveedor','fechaIngreso','banco','tipo','cuenta')

class ProveedorCuentaTabularInline(admin.TabularInline):
	model = ProveedorCuenta

class InsumoProveedorTabularInline(admin.TabularInline):
	model = InsumoProveedor
	
class ProveedorAdmin(admin.ModelAdmin):
	inlines = [ProveedorCuentaTabularInline,
			   ProveedorContactoTabularInline,
			   InsumoProveedorTabularInline,]
	list_instances = True	
	class Meta:
		model = Proveedor

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(ProveedorCuenta, ProveedorCuentaAdmin)
admin.site.register(ProveedorContacto, ProveedorContactoAdmin)
admin.site.register(InsumoProveedor)
