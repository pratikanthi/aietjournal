# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0018_labmanual_manual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmanual',
            name='semester',
            field=models.ForeignKey(to='paper.Semester'),
            preserve_default=True,
        ),
    ]
