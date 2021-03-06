# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('pid', models.UUIDField(default=uuid.uuid4, help_text='Unique ID ', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(help_text='First Name', max_length=50)),
                ('middle_initial', models.CharField(max_length=2)),
                ('last_name', models.CharField(help_text='Last Name', max_length=50)),
                ('female', models.BooleanField(default=False)),
                ('ssn4', models.CharField(max_length=4)),
                ('active_smoker', models.BooleanField(default=False)),
                ('osa', models.BooleanField(default=False)),
                ('climb2', models.BooleanField(default=False, help_text='can climb 2 flights of steps')),
                ('age', models.CharField(help_text='age', max_length=3)),
            ],
        ),
    ]
