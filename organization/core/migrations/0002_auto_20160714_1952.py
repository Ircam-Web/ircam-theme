# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 17:52
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization-core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicpage',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='basicpage',
            name='content_fr',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
    ]
