# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0016_auto_20170304_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selfvalueofmaster',
            old_name='servicevalue',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='selfmaster',
            name='master_status',
        ),
        migrations.RemoveField(
            model_name='selfvalueofmaster',
            name='sumvalue',
        ),
        migrations.RemoveField(
            model_name='selfvalueofmaster',
            name='workvalue',
        ),
    ]
