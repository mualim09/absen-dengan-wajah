# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-26 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absensi', '0005_auto_20180115_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='status',
            field=models.CharField(choices=[('H', 'Hadir'), ('A', 'Tanpa Keterangan'), ('I', 'Ijin'), ('S', 'Sakit')], default='H', max_length=1),
        ),
    ]