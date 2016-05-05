# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryh',
            name='abuses',
            field=models.ManyToManyField(related_name='habuses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='queryh',
            name='votes',
            field=models.ManyToManyField(related_name='hvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
