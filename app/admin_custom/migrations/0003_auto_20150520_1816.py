# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0002_auto_20150520_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 18, 16, 7, 762016, tzinfo=utc), verbose_name=b'date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 18, 16, 7, 761499, tzinfo=utc), verbose_name=b'last login'),
        ),
    ]
