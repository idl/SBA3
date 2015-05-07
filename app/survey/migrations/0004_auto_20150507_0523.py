# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user_id',
            new_name='uid',
        ),
    ]
