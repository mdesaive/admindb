# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0011_auto_20160310_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='itservice',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='landspace',
        ),
        migrations.RemoveField(
            model_name='container',
            name='host',
        ),
        migrations.RemoveField(
            model_name='container',
            name='itservice',
        ),
        migrations.RemoveField(
            model_name='container',
            name='landspace',
        ),
        migrations.RemoveField(
            model_name='container',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='host',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='hostmapcomputer',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='hostmapcomputer',
            name='computer',
        ),
        migrations.RemoveField(
            model_name='hostmapcomputer',
            name='role',
        ),
        migrations.RemoveField(
            model_name='vm',
            name='host',
        ),
        migrations.RemoveField(
            model_name='vm',
            name='itservice',
        ),
        migrations.RemoveField(
            model_name='vm',
            name='landspace',
        ),
        migrations.RemoveField(
            model_name='vm',
            name='technology',
        ),
        migrations.DeleteModel(
            name='Computer',
        ),
        migrations.DeleteModel(
            name='ComputerRoles',
        ),
        migrations.DeleteModel(
            name='Container',
        ),
        migrations.DeleteModel(
            name='ContainerTechnology',
        ),
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.DeleteModel(
            name='HostMapComputer',
        ),
        migrations.DeleteModel(
            name='HostTechnology',
        ),
        migrations.DeleteModel(
            name='VM',
        ),
        migrations.DeleteModel(
            name='VMTechnology',
        ),
    ]
