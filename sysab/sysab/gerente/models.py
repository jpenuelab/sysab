from django.db import models

# Create your models here.
# Tabla 8
class TbGerente(models.Model):
    id_gerente = models.AutoField(primary_key=True)
    doc_gerente = models.CharField(unique=True, max_length=20)
    nombre_gerente = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_gerente'

    def __str__(self):
        return self.nombre_gerente
