# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 13:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0025_auto_20170310_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 11, 13, 47, 7, 968784)),
        ),
    ]