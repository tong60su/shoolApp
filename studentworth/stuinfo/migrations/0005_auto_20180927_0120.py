# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-27 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuinfo', '0004_auto_20180927_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalexam',
            name='sudent_classid',
            field=models.PositiveIntegerField(default=0, verbose_name='班级'),
        ),
        migrations.AlterField(
            model_name='monthlyexam',
            name='sudent_classid',
            field=models.PositiveIntegerField(default=0, verbose_name='班级'),
        ),
    ]
