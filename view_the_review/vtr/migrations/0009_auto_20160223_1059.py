# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0008_auto_20160212_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='slug',
            field=models.CharField(default=b'query title', unique=True, max_length=100),
        ),
    ]
