# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-05 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20170605_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorganization',
            old_name='fav_nums',
            new_name='fav_num',
        ),
    ]
