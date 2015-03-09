# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0003_auto_20150210_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('semester', models.IntegerField()),
                ('branch', models.ForeignKey(to='paper.Branch')),
                ('subject', models.ForeignKey(to='paper.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
