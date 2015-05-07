# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('location', models.CharField(help_text=b'Please enter the city and state of your school.', max_length=125)),
                ('survey_title', models.CharField(max_length=50, null=True)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'School',
            },
        ),
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
