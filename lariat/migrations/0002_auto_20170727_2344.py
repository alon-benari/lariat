# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lariat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
