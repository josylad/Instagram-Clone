# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-16 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20191016_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='author_profile',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='gallery.Profile'),
        ),
    ]
