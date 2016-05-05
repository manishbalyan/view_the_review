# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0003_remove_queryh_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queryh',
            name='abuses',
        ),
    ]
