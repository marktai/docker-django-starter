# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
