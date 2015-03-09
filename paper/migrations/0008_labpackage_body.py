# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0007_labpackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='labpackage',
            name='body',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
