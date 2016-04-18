# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0015_auto_20160417_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 18), null=True),
        ),
    ]
