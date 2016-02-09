# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0002_auto_20160206_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rollnumber',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
