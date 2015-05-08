# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_remove_student_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='schooluid',
            name='school',
        ),
        migrations.RemoveField(
            model_name='schooluid',
            name='student',
        ),
        migrations.RemoveField(
            model_name='resultset',
            name='uid',
        ),
        migrations.AddField(
            model_name='student',
            name='result_set',
            field=models.OneToOneField(null=True, to='survey.ResultSet'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(default='', to='survey.School'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SchoolUid',
        ),
        migrations.AddField(
            model_name='student',
            name='uid',
            field=models.ForeignKey(default='', to='survey.Uid'),
            preserve_default=False,
        ),
    ]
