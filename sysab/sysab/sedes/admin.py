from django.contrib import admin
from .models import TbSede

# Register your models here.
class SedeAdmin(admin.ModelAdmin):
    list_display=('id_sede', 'desc_sede', 'estado')

admin.site.register(TbSede, SedeAdmin)

# Register your models here.
