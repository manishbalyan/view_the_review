# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='key_expires',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rollnumber',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
