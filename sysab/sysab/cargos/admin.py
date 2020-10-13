from django.contrib import admin
from .models import TbCargos

# Register your models here.


class CargosAdmin(admin.ModelAdmin):
    list_display=('id_cargo', 'desc_cargo', 'estado')

admin.site.register(TbCargos, CargosAdmin)