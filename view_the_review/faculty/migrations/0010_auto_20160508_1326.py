# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0009_auto_20160425_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilef',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 5, 8), null=True),
        ),
    ]
