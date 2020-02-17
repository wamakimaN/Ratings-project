# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-17 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='remark',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
