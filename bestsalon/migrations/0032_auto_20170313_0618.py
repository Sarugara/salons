# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 06:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0031_auto_20170312_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecategory',
            name='cat_desc',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='cat_logo',
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 14, 6, 18, 19, 935969)),
        ),
    ]
