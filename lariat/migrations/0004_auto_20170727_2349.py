# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lariat', '0003_auto_20170727_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='ssn',
            new_name='SSN',
        ),
    ]
