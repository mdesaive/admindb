# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itservices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='itservice',
            name='its_type',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='itservices.Type'),
            preserve_default=False,
        ),
    ]
