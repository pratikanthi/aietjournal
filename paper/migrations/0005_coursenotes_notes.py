# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0004_coursenotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursenotes',
            name='notes',
            field=models.FileField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
