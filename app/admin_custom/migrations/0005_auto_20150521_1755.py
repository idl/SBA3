# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0004_auto_20150520_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 21, 17, 55, 58, 433225, tzinfo=utc), verbose_name=b'date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 21, 17, 55, 58, 432929, tzinfo=utc), verbose_name=b'last login'),
        ),
    ]
