# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-08 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170608_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='click_num',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570'),
        ),
    ]
