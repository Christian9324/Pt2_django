# Generated by Django 2.2.5 on 2019-09-28 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puntos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=400)),
                ('latitud', models.FloatField(blank=True, default=None, null=True)),
                ('longitud', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
