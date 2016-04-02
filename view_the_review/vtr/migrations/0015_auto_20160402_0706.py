# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0014_auto_20160402_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='query',
        ),
        migrations.AddField(
            model_name='query',
            name='tag',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
