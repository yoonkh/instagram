# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=24, null=True, unique=True),
        ),
    ]
