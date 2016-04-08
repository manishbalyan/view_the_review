# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vtr.models


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0004_auto_20160408_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='profile_pic',
            field=models.ImageField(default=b'@@@@.jpg', null=True, upload_to=vtr.models.upload_to, blank=True),
        ),
    ]
