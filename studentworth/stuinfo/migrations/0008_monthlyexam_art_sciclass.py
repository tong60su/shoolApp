# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-27 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuinfo', '0007_finalexam_art_sciclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyexam',
            name='Art_SciClass',
            field=models.PositiveIntegerField(default=0, verbose_name='文理分科'),
        ),
    ]
