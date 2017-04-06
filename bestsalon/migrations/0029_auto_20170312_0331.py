# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 03:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0028_auto_20170311_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='selfworks',
            name='work_service',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bestsalon.SelfServices'),
        ),
        migrations.AddField(
            model_name='works',
            name='work_service',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bestsalon.Services'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 13, 3, 31, 1, 774716)),
        ),
    ]
