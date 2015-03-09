# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0020_auto_20150301_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='labmanual',
            name='subject',
            field=models.ForeignKey(default='a', to='paper.Subject'),
            preserve_default=False,
        ),
    ]
