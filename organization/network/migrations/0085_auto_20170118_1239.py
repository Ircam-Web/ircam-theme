# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-18 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0084_auto_20170118_1119'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personactivitytimesheet',
            unique_together=set([('activity', 'project', 'month', 'year')]),
        ),
    ]