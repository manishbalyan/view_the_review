# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_auto_20160408_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilef',
            name='activation_key',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofilef',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 14), null=True),
        ),
    ]
