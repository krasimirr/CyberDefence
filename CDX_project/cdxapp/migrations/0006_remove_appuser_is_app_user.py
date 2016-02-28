# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdxapp', '0005_auto_20160228_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='is_app_user',
        ),
    ]
