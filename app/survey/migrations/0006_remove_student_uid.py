# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_resultset_schooluid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='uid',
        ),
    ]
