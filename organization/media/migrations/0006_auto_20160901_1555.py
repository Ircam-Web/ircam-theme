# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-media', '0005_displayableaudio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='displayableaudio',
            name='audio_ptr',
        ),
        migrations.RemoveField(
            model_name='displayableaudio',
            name='displayable',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='customdisplayable_ptr',
        ),
        migrations.RemoveField(
            model_name='video',
            name='customdisplayable_ptr',
        ),
        migrations.AddField(
            model_name='audio',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='audio',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='audio',
            name='title',
            field=models.CharField(default='a', max_length=1024, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='a', max_length=1024, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audio',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='title_en',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='title_fr',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title_en',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title_fr',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.DeleteModel(
            name='DisplayableAudio',
        ),
    ]