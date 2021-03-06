# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170811_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='numDoc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Numero de Documento '),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Dirección Residencia '),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='municipality',
            field=models.CharField(blank=True, choices=[('B', 'Bucaramanga'), ('G', 'Girón'), ('F', 'Floridablanca'), ('P', 'Piedecuesta')], max_length=1, verbose_name='Municipio de Residencia '),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Número de Teléfono '),
        ),
    ]
