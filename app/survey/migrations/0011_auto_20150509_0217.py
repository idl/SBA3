# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_auto_20150509_0201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='date',
            new_name='date_created',
        ),
    ]
