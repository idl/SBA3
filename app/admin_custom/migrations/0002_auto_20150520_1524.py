# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 15, 24, 8, 117987, tzinfo=utc), verbose_name=b'date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 15, 24, 8, 117139, tzinfo=utc), verbose_name=b'last login'),
        ),
    ]
