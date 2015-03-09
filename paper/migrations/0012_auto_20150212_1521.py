# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0011_auto_20150212_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branch_code',
            field=models.CharField(default='a', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
