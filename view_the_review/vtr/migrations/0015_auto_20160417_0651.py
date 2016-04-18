# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0014_auto_20160414_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 17), null=True),
        ),
    ]
