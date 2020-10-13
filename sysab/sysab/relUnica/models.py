from django.db import models
from centroCostos.models import TbCentroCostos
from gerente.models import TbGerente
from ejecutivos.models import TbEjecutivo
from team.models import TbTeam
from empleado.models import TbEmpleado



# Create your models here.
#Tabla 10
class TbRelUnica(models.Model):
    id_rel_unica = models.AutoField(primary_key=True)
    id_cc = models.ForeignKey(TbCentroCostos, models.DO_NOTHING, db_column='id_cc')
    id_gerente = models.ForeignKey(TbGerente, models.DO_NOTHING, db_column='id_gerente')
    id_ejecutivo = models.ForeignKey(TbEjecutivo, models.DO_NOTHING, db_column='id_ejecutivo')
    id_team = models.ForeignKey(TbTeam, models.DO_NOTHING, db_column='id_team')
    id_user = models.ForeignKey(TbEmpleado, models.DO_NOTHING, db_column='id_user')
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_rel_unica'

    def __str__(self):
        return self.id_rel_unica