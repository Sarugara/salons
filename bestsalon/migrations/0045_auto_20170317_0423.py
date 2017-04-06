# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 04:23
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bestsalon', '0044_auto_20170316_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='valueofsalon',
            name='whovalueit',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 18, 4, 23, 7, 149266)),
        ),
    ]