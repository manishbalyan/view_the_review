# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtr', '0013_auto_20160308_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='query',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='query',
            field=models.ManyToManyField(to='vtr.Query'),
        ),
    ]
