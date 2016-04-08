# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vtr.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('faculty_id', models.CharField(max_length=30, null=True, blank=True)),
                ('department', models.CharField(max_length=30, null=True, blank=True)),
                ('profile_pic', models.ImageField(default=b'@@@@', null=True, upload_to=vtr.models.upload_to, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
