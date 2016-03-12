# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0010_auto_20160310_0739'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClusterRoles',
            new_name='ComputerRoles',
        ),
        migrations.RenameModel(
            old_name='Cluster',
            new_name='Host',
        ),
        migrations.RenameModel(
            old_name='ClusterMapComputer',
            new_name='HostMapComputer',
        ),
        migrations.RenameModel(
            old_name='ClusterTechnology',
            new_name='HostTechnology',
        ),
    ]
