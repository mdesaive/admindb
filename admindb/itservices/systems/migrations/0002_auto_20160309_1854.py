# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 18:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0001_initial'),
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
        migrations.DeleteModel(
            name='Computer',
        ),
    ]
