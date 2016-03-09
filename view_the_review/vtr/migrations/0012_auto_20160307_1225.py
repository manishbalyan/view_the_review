# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0011_auto_20160307_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
