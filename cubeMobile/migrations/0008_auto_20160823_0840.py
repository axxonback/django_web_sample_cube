# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubeMobile', '0007_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portoflio',
            name='type',
            field=models.CharField(choices=[('mobile', 'mobile'), ('cloud', 'cloud'), ('web', 'website'), ('desktop', 'desktop')], max_length=50),
        ),
    ]
