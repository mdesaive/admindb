# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0009_auto_20160310_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='host',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='systems.Cluster'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vm',
            name='host',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='systems.Cluster'),
            preserve_default=False,
        ),
    ]
