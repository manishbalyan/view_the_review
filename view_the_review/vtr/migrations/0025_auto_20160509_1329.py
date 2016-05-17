# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vtr.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0024_auto_20160508_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 5, 9), null=True),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='profile_pic',
            field=models.ImageField(default=b'@@@@', null=True, upload_to=vtr.models.upload_to, blank=True),
        ),
    ]
