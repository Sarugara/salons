# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 05:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bestsalon', '0019_auto_20170306_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='wholikeit',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
