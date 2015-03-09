# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0016_auto_20150216_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='labpackage',
            name='title_slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
    ]
