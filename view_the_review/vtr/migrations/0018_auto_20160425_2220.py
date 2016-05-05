# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0017_auto_20160418_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='userDownVotes',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='userUpVotes',
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 25), null=True),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='profile_pic',
            field=models.ImageField(default=b'images/@@@@.jpg', upload_to=b'images'),
        ),
    ]
