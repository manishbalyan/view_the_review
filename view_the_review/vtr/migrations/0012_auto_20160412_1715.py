# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0011_auto_20160412_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='hostler',
            field=models.BooleanField(default=0),
        ),
    ]
