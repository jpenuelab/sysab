# Generated by Django 3.1 on 2020-09-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbEjecutivo',
            fields=[
                ('id_ejecutivo', models.AutoField(primary_key=True, serialize=False)),
                ('doc_ejecutivo', models.CharField(max_length=20, unique=True)),
                ('nombre_ejecutivo', models.CharField(max_length=120)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_ejecutivo',
            },
        ),
    ]
