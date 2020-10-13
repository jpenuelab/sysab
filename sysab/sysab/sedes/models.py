from django.db import models

# Create your models here.
class TbSede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    desc_sede = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        db_table = 'tb_sede'

    def __str__(self):
        return self.desc_sede