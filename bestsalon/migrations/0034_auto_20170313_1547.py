# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 15:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0033_auto_20170313_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 14, 15, 47, 34, 573898)),
        ),
        migrations.RemoveField(
            model_name='works',
            name='work_service',
        ),
        migrations.AddField(
            model_name='works',
            name='work_service',
            field=models.ManyToManyField(to='bestsalon.Services'),
        ),
    ]
