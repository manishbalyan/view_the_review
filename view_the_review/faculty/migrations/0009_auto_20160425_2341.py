# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vtr.models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0008_auto_20160425_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilef',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=vtr.models.upload_to, blank=True),
        ),
    ]
