# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0015_auto_20150216_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labpackage',
            name='semester',
            field=models.ForeignKey(to='paper.Semester'),
            preserve_default=True,
        ),
    ]
