# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-08 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20170607_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='work_position',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='work_years',
        ),
    ]
