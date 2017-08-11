# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='firsrtName',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='municipality',
            field=models.CharField(blank=True, choices=[('B', 'Bucaramanga'), ('G', 'Girón'), ('F', 'Floridablanca'), ('P', 'Piedecuesta')], max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.PositiveIntegerField(blank=True, max_length=20),
        ),
    ]
