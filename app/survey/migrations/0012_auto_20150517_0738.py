# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_auto_20150509_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_completed',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p1',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p10',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p11',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p2',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p3',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p4',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p5',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p6',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p7',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p8',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='p9',
            field=jsonfield.fields.JSONField(),
        ),
    ]
