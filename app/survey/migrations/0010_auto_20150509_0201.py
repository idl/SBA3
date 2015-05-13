# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_auto_20150508_2115'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='resultset',
            table='ResultSet',
        ),
    ]
