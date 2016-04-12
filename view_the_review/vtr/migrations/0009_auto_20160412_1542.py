# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0008_auto_20160412_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='activation_key',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='key_expires',
            field=models.DateTimeField(null=True),
        ),
    ]
