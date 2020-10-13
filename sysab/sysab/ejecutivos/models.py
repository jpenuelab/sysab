from django.db import models
# Create your models here.
# Tabla 5
class TbEjecutivo(models.Model):
    id_ejecutivo = models.AutoField(primary_key=True)
    doc_ejecutivo = models.CharField(unique=True, max_length=20)
    nombre_ejecutivo = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_ejecutivo'

    def __str__(self):
        return self.nombre_ejecutivo