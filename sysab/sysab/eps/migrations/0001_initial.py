# Generated by Django 3.1 on 2020-09-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbEps',
            fields=[
                ('id_eps', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_eps', models.CharField(max_length=120)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_eps',
            },
        ),
    ]
