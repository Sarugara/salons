# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestsalon', '0007_auto_20170223_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_name', models.CharField(max_length=250)),
                ('master_desc', models.CharField(max_length=500)),
                ('master_logo', models.ImageField(default=b'masters/noname.jpg', upload_to=b'masters/')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestsalon.Salons')),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_desc', models.CharField(max_length=250)),
                ('work_logo', models.ImageField(upload_to=b'works/')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestsalon.Salons')),
            ],
        ),
    ]
