# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0002_auto_20170223_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salons',
            name='salon_logo',
            field=models.ImageField(default=b'media/no.jpg', upload_to=b'media/'),
        ),
    ]
