# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0017_auto_20160312_1026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clustermapcomputer',
            options={},
        ),
        migrations.RemoveField(
            model_name='clustermapcomputer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='clustermapcomputer',
            name='itservice',
        ),
        migrations.RemoveField(
            model_name='clustermapcomputer',
            name='landspace',
        ),
        migrations.RemoveField(
            model_name='clustermapcomputer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='clustermapcomputer',
            name='note',
        ),
    ]
