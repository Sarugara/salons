# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 05:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0042_auto_20170316_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 17, 5, 2, 26, 72971)),
        ),
    ]
