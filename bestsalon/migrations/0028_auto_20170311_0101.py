# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 01:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0027_auto_20170311_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 12, 1, 1, 10, 288171)),
        ),
        migrations.AlterField(
            model_name='book',
            name='flag',
            field=models.IntegerField(default=1),
        ),
    ]
