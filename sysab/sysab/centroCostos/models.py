from django.db import models
from sedes.models import TbSede


# Create your models here.

# Tabla 4
class TbCentroCostos(models.Model):
    id_cc = models.AutoField(primary_key=True)
    codigo = models.IntegerField(unique=True)
    nombre_cc = models.CharField(max_length=120)
    sede = models.ForeignKey(TbSede, models.DO_NOTHING, db_column='sede')
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_centro_costos'

    def __str__(self):
        return self.nombre_cc