# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20150411_0448'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='Student',
        ),
    ]
