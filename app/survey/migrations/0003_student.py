# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20150507_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('continue_pass', models.CharField(max_length=10)),
                ('completed', models.BooleanField()),
                ('school', models.ForeignKey(to='survey.School', null=True)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
