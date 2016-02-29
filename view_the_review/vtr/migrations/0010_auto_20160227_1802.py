# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0009_auto_20160223_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='slug',
            field=models.SlugField(),
        ),
    ]
