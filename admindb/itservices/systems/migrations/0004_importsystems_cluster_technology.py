# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0003_auto_20160330_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='importsystems',
            name='cluster_technology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.ClusterTechnology'),
        ),
    ]