from django.db import models

# Create your models here.
# Tabla 6
class TbEps(models.Model):
    id_eps = models.AutoField(primary_key=True)
    nombre_eps = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_eps'

    def __str__(self):
        return self.nombre_eps