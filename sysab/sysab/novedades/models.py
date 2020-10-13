from django.db import models
from django.contrib.auth.models import User
from relUnica.models import TbRelUnica
from cie10.models import Cie10
# Create your models here.
# Tabla 11
class TbNovedades(models.Model):
    id_novedad = models.AutoField(primary_key=True)
    id_rel_unica = models.ForeignKey(TbRelUnica, models.DO_NOTHING, db_column='id_rel_unica')
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    incapacidad = models.CharField(max_length=120)
    cod_cie = models.ForeignKey(Cie10, models.DO_NOTHING, db_column='cod_cie')
    prorroga_ini = models.CharField(max_length=120)
    id_novedad_pro = models.IntegerField()
    # user_reg = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_reg')
    user_reg = models.ForeignKey(User,verbose_name="User_reg",on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField()
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_novedades'

    def __str__(self):
        return self.id_novedad