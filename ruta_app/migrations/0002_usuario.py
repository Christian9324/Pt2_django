# Generated by Django 2.2.5 on 2019-12-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruta_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=150)),
                ('correo', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]