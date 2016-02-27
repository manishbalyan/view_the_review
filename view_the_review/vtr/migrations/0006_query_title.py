# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0005_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='title',
            field=models.CharField(default=b'title', max_length=100),
        ),
    ]
