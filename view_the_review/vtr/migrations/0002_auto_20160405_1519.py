# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querys',
            name='title',
            field=models.CharField(default=b'title', unique=True, max_length=100),
        ),
    ]
