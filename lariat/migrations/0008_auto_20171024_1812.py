# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-24 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lariat', '0007_patient_osaa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='osaa',
        ),
        migrations.AddField(
            model_name='patient',
            name='nephrologist',
            field=models.BooleanField(default=False),
        ),
    ]
