from django.contrib import admin
from .models import *
from .lenguaje import *

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre_user', 'usuario')
    search_fields = ('nombre_user', 'usuario__username', 'usuario__first_name', 'usuario__last_name')

# Register your models here.
admin.site.register(Perfil, PerfilAdmin)

admin.site.site_header = titulo_sistema
admin.site.index_title = "Panel de administración"
admin.site.site_title = "Sitio administrativo"
