# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-03 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0005_auto_20180803_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='type',
            field=models.CharField(blank=True, choices=[('KEY', 'KEY'), ('PRIMARY KEY', 'PRIMARY KEY'), ('UNIQUE KEY', 'UNIQUE KEY')], help_text='\u7c7b\u578b', max_length=100, null=True),
        ),
    ]
