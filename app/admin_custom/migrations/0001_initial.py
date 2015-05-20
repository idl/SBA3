# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_student_email'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('password', models.CharField(max_length=128, verbose_name=b'password')),
                ('last_login', models.DateTimeField(default=datetime.datetime(2015, 5, 20, 15, 23, 35, 745508, tzinfo=utc), verbose_name=b'last login')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'email address')),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2015, 5, 20, 15, 23, 35, 746147, tzinfo=utc), verbose_name=b'date joined')),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('school', models.ForeignKey(to='survey.School', null=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name_plural': 'users',
            },
        ),
    ]
