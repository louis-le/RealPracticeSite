# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0008_auto_20160613_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='utility',
            name='link',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
