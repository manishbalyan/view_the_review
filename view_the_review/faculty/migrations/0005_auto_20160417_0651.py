# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_auto_20160414_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilef',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 17), null=True),
        ),
    ]
