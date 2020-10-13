from django.contrib import admin
from .models import TbCentroCostos

# Register your models here.
class CentroCostosAdmin(admin.ModelAdmin):
    list_display=('id_cc', 'codigo', 'nombre_cc','sede','estado')

admin.site.register(TbCentroCostos, CentroCostosAdmin)