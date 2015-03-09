# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpaper',
            name='qpaper',
            field=models.FileField(default='q', upload_to=b'media/'),
            preserve_default=False,
        ),
    ]
