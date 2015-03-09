# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0019_auto_20150217_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursenotes',
            name='semester',
            field=models.ForeignKey(to='paper.Semester'),
            preserve_default=True,
        ),
    ]
