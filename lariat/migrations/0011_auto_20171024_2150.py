# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-24 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lariat', '0010_auto_20171024_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(help_text='age'),
        ),
    ]
