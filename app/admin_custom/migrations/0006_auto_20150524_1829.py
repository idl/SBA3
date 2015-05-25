# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0005_auto_20150521_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 24, 18, 29, 34, 557057, tzinfo=utc), verbose_name=b'date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 24, 18, 29, 34, 556711, tzinfo=utc), verbose_name=b'last login'),
        ),
    ]
