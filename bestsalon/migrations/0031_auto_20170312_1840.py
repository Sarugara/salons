# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 18:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0030_auto_20170312_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selfmaster',
            old_name='salon_book',
            new_name='master_book',
        ),
        migrations.RenameField(
            model_name='selfmaster',
            old_name='salon_feedback',
            new_name='master_feedback',
        ),
        migrations.AddField(
            model_name='selfmaster',
            name='master_services',
            field=models.ManyToManyField(to='bestsalon.Services'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 13, 18, 40, 31, 181782)),
        ),
    ]