# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vtr.models


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0020_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='querys',
            name='image',
            field=models.ImageField(null=True, upload_to=vtr.models.upload_to, blank=True),
        ),
    ]
