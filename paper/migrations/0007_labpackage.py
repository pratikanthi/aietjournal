# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0006_labmanual'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabPackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('semester', models.IntegerField()),
                ('branch', models.ForeignKey(to='paper.Branch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
