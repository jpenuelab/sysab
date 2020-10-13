from django.db import models

# Create your models here.

# Tabla 1
class Cie10(models.Model):
    id_cie = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        db_table = 'cie10'

    def __str__(self):
        return self.descripcion 