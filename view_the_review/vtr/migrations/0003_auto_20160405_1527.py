# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0002_auto_20160405_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querys',
            name='title',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
