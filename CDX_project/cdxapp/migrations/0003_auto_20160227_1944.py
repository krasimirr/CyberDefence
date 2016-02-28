# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cdxapp', '0002_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='username',
        ),
        migrations.AddField(
            model_name='appuser',
            name='balance',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appuser',
            name='fname',
            field=models.CharField(default=datetime.date(2016, 2, 27), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='lname',
            field=models.CharField(default=datetime.date(2016, 2, 27), max_length=300),
            preserve_default=False,
        ),
    ]
