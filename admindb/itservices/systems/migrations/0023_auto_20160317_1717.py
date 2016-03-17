# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0022_importsystemsaggregated_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='importsystemsaggregated',
            name='tag3',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='importsystemsaggregated',
            name='tag1',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='importsystemsaggregated',
            name='tag2',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]
