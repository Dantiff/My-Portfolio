# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20170607_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
