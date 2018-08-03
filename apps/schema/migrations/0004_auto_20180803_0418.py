# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-03 04:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0003_auto_20180803_0315'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='column',
            unique_together=set([('table', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='index',
            unique_together=set([('table', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='table',
            unique_together=set([('database', 'name')]),
        ),
    ]
