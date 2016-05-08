# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0023_auto_20160425_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='i_agree',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 5, 8), null=True),
        ),
    ]
