# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_questionpaper_qpaper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpaper',
            name='qpaper',
            field=models.FileField(upload_to=b''),
            preserve_default=True,
        ),
    ]
