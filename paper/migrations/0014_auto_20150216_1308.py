# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0013_subject_subject_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='id',
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_code',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
