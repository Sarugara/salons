# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0014_auto_20170302_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='valueofsalon',
            name='servicevalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='valueofsalon',
            name='workvalue',
            field=models.IntegerField(default=0),
        ),
    ]
