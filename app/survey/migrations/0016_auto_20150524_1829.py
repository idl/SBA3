# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0015_resultset_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 5, 24, 18, 29, 34, 553996)),
        ),
        migrations.AlterField(
            model_name='school',
            name='location',
            field=models.CharField(help_text=b'Please enter the city and state of the school.', max_length=125),
        ),
        migrations.AlterField(
            model_name='school',
            name='survey_title',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
    ]
