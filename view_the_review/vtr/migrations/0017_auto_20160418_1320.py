# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vtr', '0016_auto_20160418_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userDownVotes', models.ManyToManyField(related_name='threadDownVotes', to=settings.AUTH_USER_MODEL, blank=True)),
                ('userUpVotes', models.ManyToManyField(related_name='threadUpVotes', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='querys',
            name='votes',
        ),
    ]
