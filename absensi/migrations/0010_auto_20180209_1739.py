# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-09 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absensi', '0009_auto_20180209_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='waktu_keluar',
            field=models.DateTimeField(blank=True),
        ),
    ]
