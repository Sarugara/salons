# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 19:03
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bestsalon', '0049_auto_20170318_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selfvalueofmaster',
            old_name='value',
            new_name='servicevalue',
        ),
        migrations.AddField(
            model_name='selfvalueofmaster',
            name='sumvalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='selfvalueofmaster',
            name='whovalueit',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='selfvalueofmaster',
            name='workvalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 19, 19, 3, 14, 755578)),
        ),
    ]
