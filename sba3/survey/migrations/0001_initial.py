# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('p1q1', models.CharField(max_length=20, null=True)),
                ('p1q2', models.CharField(max_length=20, null=True)),
                ('p1q3', models.CharField(max_length=20, null=True)),
                ('p1q4', models.CharField(max_length=20, null=True)),
                ('p1q5', models.CharField(max_length=20, null=True)),
                ('p1q6', models.CharField(max_length=20, null=True)),
                ('p1q7', models.CharField(max_length=20, null=True)),
                ('p1q8', models.CharField(max_length=20, null=True)),
                ('p1q9', models.CharField(max_length=20, null=True)),
                ('p1q10', models.CharField(max_length=20, null=True)),
                ('p1q11', models.CharField(max_length=20, null=True)),
                ('p2q1', models.CharField(max_length=20, null=True)),
                ('p2q2', models.CharField(max_length=20, null=True)),
                ('p2q3', models.CharField(max_length=20, null=True)),
                ('p2q4', models.CharField(max_length=20, null=True)),
                ('p2q5', models.CharField(max_length=20, null=True)),
                ('p2q6', models.CharField(max_length=20, null=True)),
                ('p2q7', models.CharField(max_length=20, null=True)),
                ('p2q8', models.CharField(max_length=20, null=True)),
                ('p2q9', models.CharField(max_length=20, null=True)),
                ('p2q10', models.CharField(max_length=20, null=True)),
                ('p2q11', models.CharField(max_length=20, null=True)),
                ('p3q1', models.CharField(max_length=20, null=True)),
                ('p3q2', models.CharField(max_length=20, null=True)),
                ('p3q3', models.CharField(max_length=20, null=True)),
                ('p3q4', models.CharField(max_length=20, null=True)),
                ('p3q5', models.CharField(max_length=20, null=True)),
                ('p3q6', models.CharField(max_length=20, null=True)),
                ('p3q7', models.CharField(max_length=20, null=True)),
                ('p3q8', models.CharField(max_length=20, null=True)),
                ('p3q9', models.CharField(max_length=20, null=True)),
                ('p4q1', models.CharField(max_length=20, null=True)),
                ('p4q2', models.CharField(max_length=20, null=True)),
                ('p4q3', models.CharField(max_length=20, null=True)),
                ('p4q4', models.CharField(max_length=20, null=True)),
                ('p4q5', models.CharField(max_length=20, null=True)),
                ('p4q6', models.CharField(max_length=20, null=True)),
                ('p4q7', models.CharField(max_length=20, null=True)),
                ('p4q8', models.CharField(max_length=20, null=True)),
                ('p4q9', models.CharField(max_length=20, null=True)),
                ('p4q10', models.CharField(max_length=20, null=True)),
                ('p4q11', models.CharField(max_length=20, null=True)),
                ('p5q1', models.CharField(max_length=20, null=True)),
                ('p5q2', models.CharField(max_length=20, null=True)),
                ('p5q3', models.CharField(max_length=20, null=True)),
                ('p5q4', models.CharField(max_length=20, null=True)),
                ('p5q5', models.CharField(max_length=20, null=True)),
                ('p5q6', models.CharField(max_length=20, null=True)),
                ('p5q7', models.CharField(max_length=20, null=True)),
                ('p5q8', models.CharField(max_length=20, null=True)),
                ('p5q9', models.CharField(max_length=20, null=True)),
                ('p5q10', models.CharField(max_length=20, null=True)),
                ('p5q11', models.CharField(max_length=20, null=True)),
                ('p5q12', models.CharField(max_length=20, null=True)),
                ('p5q13', models.CharField(max_length=20, null=True)),
                ('p5q14', models.CharField(max_length=20, null=True)),
                ('p6q1', models.CharField(max_length=20, null=True)),
                ('p6q2', models.CharField(max_length=20, null=True)),
                ('p6q3', models.CharField(max_length=20, null=True)),
                ('p6q4', models.CharField(max_length=20, null=True)),
                ('p6q5', models.CharField(max_length=20, null=True)),
                ('p6q6', models.CharField(max_length=20, null=True)),
                ('p6q7', models.CharField(max_length=20, null=True)),
                ('p6q8', models.CharField(max_length=20, null=True)),
                ('p6q9', models.CharField(max_length=20, null=True)),
                ('p6q10', models.CharField(max_length=20, null=True)),
                ('p6q11', models.CharField(max_length=20, null=True)),
                ('p6q12', models.CharField(max_length=20, null=True)),
                ('p7q1', models.CharField(max_length=20, null=True)),
                ('p7q2', models.CharField(max_length=20, null=True)),
                ('p7q3', models.CharField(max_length=20, null=True)),
                ('p7q4', models.CharField(max_length=20, null=True)),
                ('p7q5', models.CharField(max_length=20, null=True)),
                ('p7q6', models.CharField(max_length=20, null=True)),
                ('p7q7', models.CharField(max_length=20, null=True)),
                ('p7q8', models.CharField(max_length=20, null=True)),
                ('p7q9', models.CharField(max_length=20, null=True)),
                ('p8q1', models.CharField(max_length=20, null=True)),
                ('p8q2', models.CharField(max_length=20, null=True)),
                ('p8q3', models.CharField(max_length=20, null=True)),
                ('p8q4', models.CharField(max_length=20, null=True)),
                ('p8q5', models.CharField(max_length=20, null=True)),
                ('p8q6', models.CharField(max_length=20, null=True)),
                ('p8q7', models.CharField(max_length=20, null=True)),
                ('p8q8', models.CharField(max_length=20, null=True)),
                ('p8q9', models.CharField(max_length=20, null=True)),
                ('p8q10', models.CharField(max_length=20, null=True)),
                ('p8q11', models.CharField(max_length=20, null=True)),
                ('p8q12', models.CharField(max_length=20, null=True)),
                ('p9q1', models.CharField(max_length=20, null=True)),
                ('p9q2', models.CharField(max_length=20, null=True)),
                ('p9q3', models.CharField(max_length=20, null=True)),
                ('p9q4', models.CharField(max_length=20, null=True)),
                ('p9q5', models.CharField(max_length=20, null=True)),
                ('p9q6', models.CharField(max_length=20, null=True)),
                ('p9q7', models.CharField(max_length=20, null=True)),
                ('p9q8', models.CharField(max_length=20, null=True)),
                ('p9q9', models.CharField(max_length=20, null=True)),
                ('p9q10', models.CharField(max_length=20, null=True)),
                ('p9q11', models.CharField(max_length=20, null=True)),
                ('p9q12', models.CharField(max_length=20, null=True)),
                ('p9q13', models.CharField(max_length=20, null=True)),
                ('p10q1', models.CharField(max_length=2, null=True)),
                ('p10q2', models.CharField(max_length=2, null=True)),
                ('p10q3', models.CharField(max_length=2, null=True)),
                ('p10q4', models.CharField(max_length=2, null=True)),
                ('p10q5', models.CharField(max_length=2, null=True)),
                ('p10q6', models.CharField(max_length=2, null=True)),
                ('p10q7', models.TextField(max_length=255, null=True)),
                ('p10q8', models.TextField(max_length=255, null=True)),
                ('p10q9', models.TextField(max_length=255, null=True)),
                ('p10q10', models.TextField(max_length=255, null=True)),
                ('p10q11', models.TextField(max_length=255, null=True)),
                ('p10q12', models.TextField(max_length=255, null=True)),
                ('p11q1', models.CharField(max_length=20, null=True)),
                ('p11q2', models.CharField(max_length=20, null=True)),
                ('p11q3', models.CharField(max_length=20, null=True)),
                ('p11q4', models.CharField(max_length=20, null=True)),
                ('p11q5', models.CharField(max_length=20, null=True)),
                ('p11q6', models.CharField(max_length=20, null=True)),
                ('p11q7', models.CharField(max_length=20, null=True)),
                ('p11q8', models.CharField(max_length=20, null=True)),
                ('p11q9', models.CharField(max_length=20, null=True)),
                ('p11q10', models.CharField(max_length=20, null=True)),
                ('p11q11', models.CharField(max_length=20, null=True)),
                ('p11q12', models.CharField(max_length=20, null=True)),
                ('p11q13', models.CharField(max_length=20, null=True)),
                ('p11q14', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('location', models.CharField(help_text=b'Please enter the city and state of your school.', max_length=125)),
                ('survey_title', models.CharField(max_length=50, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolUid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=20)),
                ('school_id', models.ForeignKey(to='survey.School')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('continue_pass', models.CharField(max_length=10)),
                ('completed', models.BooleanField()),
                ('school_id', models.ForeignKey(to='survey.School', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='answerset',
            name='student_id',
            field=models.ForeignKey(to='survey.Student'),
        ),
    ]
