# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probtune', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queryp',
            old_name='pabuses',
            new_name='abuses',
        ),
        migrations.RenameField(
            model_name='queryp',
            old_name='pvotes',
            new_name='votes',
        ),
    ]
