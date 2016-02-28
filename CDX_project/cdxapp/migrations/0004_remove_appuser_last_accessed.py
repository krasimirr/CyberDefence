# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdxapp', '0003_auto_20160227_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='last_accessed',
        ),
    ]
