# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20150508_0423'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='uid',
            table='Uid',
        ),
    ]
