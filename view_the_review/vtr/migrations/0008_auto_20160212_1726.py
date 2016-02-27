# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0007_query_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='slug',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
