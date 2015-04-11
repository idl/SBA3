# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20150411_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooluid',
            name='school_id',
        ),
        migrations.DeleteModel(
            name='SchoolUid',
        ),
    ]
