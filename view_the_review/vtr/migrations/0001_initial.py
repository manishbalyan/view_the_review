# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vtr.models
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'title', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('show_user', models.BooleanField(default=0)),
                ('branch', models.CharField(max_length=20, null=True, blank=True)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('abuses', models.ManyToManyField(related_name='abusess', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('votes', models.ManyToManyField(related_name='votess', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rollnumber', models.PositiveIntegerField(null=True, blank=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('branch', models.CharField(max_length=30, null=True, blank=True)),
                ('hostler', models.BooleanField()),
                ('profile_pic', models.ImageField(null=True, upload_to=vtr.models.upload_to, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
