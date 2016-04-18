# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0013_auto_20160413_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 14), null=True),
        ),
    ]
