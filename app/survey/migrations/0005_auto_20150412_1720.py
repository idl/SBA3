# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20150411_0450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultset',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_id',
        ),
        migrations.DeleteModel(
            name='ResultSet',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
