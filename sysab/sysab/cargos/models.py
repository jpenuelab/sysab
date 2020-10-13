from django.db import models

# Create your models here.

# Tabla 2
class TbCargos(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    desc_cargo = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_cargos'

    def __str__(self):
        return self.desc_cargo