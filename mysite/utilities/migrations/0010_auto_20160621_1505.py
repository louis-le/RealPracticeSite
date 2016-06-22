# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0009_utility_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='users_sort',
            field=models.IntegerField(choices=[(1, 'Alphabetically Sorted'), (-1, 'Inverted Alphabetically Sorted'), (2, 'Login Date Sorted'), (-2, 'Inverted Login Date Sorted'), (3, 'Date Joined Sorted'), (-3, 'Inverted Date Joined Sorted')], default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='utilities_sort',
            field=models.IntegerField(choices=[(1, 'Alphabetically Sorted'), (-1, 'Inverted Alphabetically Sorted')], default=1),
        ),
    ]