# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-06 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_details_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='id',
        ),
        migrations.AlterField(
            model_name='details',
            name='user_id',
            field=models.CharField(default=0, max_length=20, primary_key=True, serialize=False),
        ),
    ]