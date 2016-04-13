# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0012_auto_20160412_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querys',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 13), null=True),
        ),
    ]
