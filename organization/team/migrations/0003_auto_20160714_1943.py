# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-team', '0002_auto_20160714_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_title',
            new_name='title',
        ),
    ]