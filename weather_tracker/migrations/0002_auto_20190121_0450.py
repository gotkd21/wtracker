# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-21 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forecast',
            name='currentpressure',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='currentpressure',
        ),
        migrations.AlterField(
            model_name='forecast',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]