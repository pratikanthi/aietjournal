# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0009_auto_20150210_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursenotes',
            options={'verbose_name_plural': 'Course notes'},
        ),
    ]
