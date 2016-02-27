# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0006_query_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='slug',
            field=models.CharField(default=b'test', max_length=100),
        ),
    ]
