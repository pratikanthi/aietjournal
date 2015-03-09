# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0010_auto_20150210_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester_no', models.IntegerField(max_length=1)),
                ('semester_name', models.CharField(max_length=20)),
                ('no_of_subjects', models.IntegerField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Semesters',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='semester',
            field=models.ForeignKey(to='paper.Semester'),
            preserve_default=True,
        ),
    ]
