# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_auto_20160424_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queryh',
            name='votes',
        ),
    ]
