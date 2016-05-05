# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0021_querys_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
