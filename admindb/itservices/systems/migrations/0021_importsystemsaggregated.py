# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itservices', '0002_auto_20160308_2022'),
        ('systems', '0020_auto_20160317_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportSystemsAggregated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('note', models.TextField(blank=True)),
                ('tag1', models.CharField(max_length=75)),
                ('tag2', models.CharField(max_length=75)),
                ('itservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itservices.ITService')),
                ('landspace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.Landspace')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
