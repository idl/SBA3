# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_completed',
        ),
        migrations.RemoveField(
            model_name='student',
            name='result_set',
        ),
        migrations.AddField(
            model_name='resultset',
            name='student',
            field=models.ForeignKey(default=None, to='survey.Student'),
        ),
        migrations.AddField(
            model_name='resultset',
            name='year',
            field=models.PositiveSmallIntegerField(default=2015),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.CharField(max_length=25),
        ),
        migrations.DeleteModel(
            name='Uid',
        ),
    ]
