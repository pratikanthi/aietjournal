# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0017_labpackage_title_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='labmanual',
            name='manual',
            field=models.FileField(default='q', upload_to=b'media/lab-manuals'),
            preserve_default=False,
        ),
    ]
