# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0010_auto_20160412_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofiles',
            options={'verbose_name_plural': 'User profiles'},
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='activation_key',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 4, 12), null=True),
        ),
    ]
