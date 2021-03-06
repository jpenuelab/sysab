# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `# managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


# Tabla 1
class Cie10(models.Model):
    id_cie = models.AutoField(primary_key=True) 
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'cie10'

# Tabla 2
class TbCargos(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    desc_cargo = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_cargos'

# Tabla 3
class TbSede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    desc_sede = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_sede'

# Tabla 4
class TbCentroCostos(models.Model):
    id_cc = models.AutoField(primary_key=True)
    codigo = models.IntegerField(unique=True)
    nombre_cc = models.CharField(max_length=120)
    sede = models.ForeignKey('TbSede', models.DO_NOTHING, db_column='sede')
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_centro_costos'

# Tabla 5
class TbEjecutivo(models.Model):
    id_ejecutivo = models.AutoField(primary_key=True)
    doc_ejecutivo = models.CharField(unique=True, max_length=20)
    nombre_ejecutivo = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_ejecutivo'

# Tabla 6
class TbEps(models.Model):
    id_eps = models.AutoField(primary_key=True)
    nombre_eps = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_eps'


# Tabla 7
class TbEmpleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    doc_empleado = models.CharField(unique=True, max_length=20)
    nombre_empleado = models.CharField(max_length=120)
    id_cargo = models.ForeignKey(TbCargos, models.DO_NOTHING, db_column='id_cargo')
    id_eps = models.ForeignKey('TbEps', models.DO_NOTHING, db_column='id_eps')
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_empleado'



# Tabla 8
class TbGerente(models.Model):
    id_gerente = models.AutoField(primary_key=True)
    doc_gerente = models.CharField(unique=True, max_length=20)
    nombre_gerente = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_gerente'

# Tabla 9 
class TbTeam(models.Model):
    id_team = models.AutoField(primary_key=True)
    doc_team = models.CharField(unique=True, max_length=20)
    nombre_team = models.CharField(max_length=120)
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_team'

#Tabla 10
class TbRelUnica(models.Model):
    id_rel_unica = models.AutoField(primary_key=True)
    id_cc = models.ForeignKey(TbCentroCostos, models.DO_NOTHING, db_column='id_cc')
    id_gerente = models.ForeignKey(TbGerente, models.DO_NOTHING, db_column='id_gerente')
    id_ejecutivo = models.ForeignKey(TbEjecutivo, models.DO_NOTHING, db_column='id_ejecutivo')
    id_team = models.ForeignKey('TbTeam', models.DO_NOTHING, db_column='id_team')
    id_user = models.ForeignKey(TbEmpleado, models.DO_NOTHING, db_column='id_user')
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'tb_rel_unica'

# Tabla 11
class TbNovedades(models.Model):
    id_novedad = models.AutoField(primary_key=True)
    id_rel_unica = models.ForeignKey('TbRelUnica', models.DO_NOTHING, db_column='id_rel_unica')
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
        # managed = False
        db_table = 'tb_novedades'










# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     last_login = models.DateTimeField()
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         # managed = False
#         db_table = 'users'


# class UsersAuthentication(models.Model):
#     users_id = models.IntegerField()
#     token = models.CharField(max_length=255)
#     expired_at = models.DateTimeField()
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         # managed = False
#         db_table = 'users_authentication'
