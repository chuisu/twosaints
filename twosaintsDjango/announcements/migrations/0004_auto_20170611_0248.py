# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 02:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_auto_20170611_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 11, 2, 48, 25, 669672)),
        ),
    ]
