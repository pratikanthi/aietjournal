# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0014_auto_20150216_1308'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='questionpaper',
            unique_together=set([('subject', 'year')]),
        ),
    ]
