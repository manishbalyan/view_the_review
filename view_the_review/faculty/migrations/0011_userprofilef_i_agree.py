# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0010_auto_20160508_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilef',
            name='i_agree',
            field=models.BooleanField(default=0),
        ),
    ]
