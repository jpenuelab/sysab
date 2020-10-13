from django.db import models

# Create your models here.
# Tabla 9 
class TbTeam(models.Model):
    id_team = models.AutoField(primary_key=True)
    doc_team = models.CharField(unique=True, max_length=20)
    nombre_team = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_team'

    def __str__(self):
        return self.nombre_team