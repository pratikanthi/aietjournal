# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0021_labmanual_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='is_a_lab',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
