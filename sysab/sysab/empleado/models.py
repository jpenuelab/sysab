from django.db import models
from cargos.models import TbCargos
from eps.models import TbEps
# Create your models here.

# Tabla 7
class TbEmpleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    doc_empleado = models.CharField(unique=True, max_length=20)
    nombre_empleado = models.CharField(max_length=120)
    id_cargo = models.ForeignKey(TbCargos, models.DO_NOTHING, db_column='id_cargo')
    id_eps = models.ForeignKey(TbEps, models.DO_NOTHING, db_column='id_eps')
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_empleado'

    def __str__(self):
        return self.nombre_empleado

