# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probtune', '0002_auto_20160424_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queryp',
            name='abuses',
        ),
        migrations.RemoveField(
            model_name='queryp',
            name='votes',
        ),
    ]
