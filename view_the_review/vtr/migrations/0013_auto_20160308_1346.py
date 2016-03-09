# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0012_auto_20160307_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='title',
            field=models.CharField(default=b'title', unique=True, max_length=100),
        ),
    ]
