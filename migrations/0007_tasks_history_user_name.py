# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0006_auto_20170220_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks_history',
            name='user_name',
            field=models.CharField(default='Luke Clarke', max_length=255),
            preserve_default=False,
        ),
    ]
