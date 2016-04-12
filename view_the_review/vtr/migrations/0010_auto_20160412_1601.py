# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0009_auto_20160412_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='userprofiles',
            name='key_expires',
        ),
    ]
