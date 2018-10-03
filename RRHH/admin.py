from django.contrib import admin

from RRHH.models import EmpleadoCargo
from RRHH.models import Organigrama
from RRHH.models import Empleado

admin.site.site_header = "NEW ANGEL administrador"
admin.site.site_title = "New Angel Portal administrativo"
admin.site.index_title = "New Angel Admin"

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, AppIndexDashboard, Dashboard

class MyAppIndexDashboard(AppIndexDashboard):

    # we don't want a title, it's redundant
    title = ''

    def __init__(self, app_title, models, **kwargs):
        AppIndexDashboard.__init__(self, app_title, models, **kwargs)

        # append a model list module that lists all models
        # for the app and a recent actions module for the current app
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                include_list=self.models,
                limit=5
            )
        ]

class MyDashboard(Dashboard):
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        # will only list the django.contrib apps
        self.children.append(modules.Feed(
            title=_('Latest Django News'),
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5
        ))
#class MyAdminClass(admin.ModelAdmin): 
#  class Media: 
#    css = { 
#      "all": ("myproject.css",) 
#    } 

class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('codigo','activo','nombre','cedula','telefonos')
	filter_horizontal = ('cargos',)
	class Meta:
		app_label = 'myapp'

class EmpleadoCargoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

#class EmpleadoCargoTabularInline(admin.TabularInline):
#	model = EmpleadoCargo
	
class OrganigramaAdmin(admin.ModelAdmin):
	filter_horizontal = ('cargosBajoMando',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(EmpleadoCargo, EmpleadoCargoAdmin)
admin.site.register(Organigrama, OrganigramaAdmin)
