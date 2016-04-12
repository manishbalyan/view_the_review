# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0007_auto_20160408_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='profile_pic',
            field=models.ImageField(default=b'images/@@@@.jpg', null=True, upload_to=b'images', blank=True),
        ),
    ]
