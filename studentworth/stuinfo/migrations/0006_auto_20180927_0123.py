# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-27 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuinfo', '0005_auto_20180927_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyexam',
            name='finalexamnum',
        ),
        migrations.AddField(
            model_name='monthlyexam',
            name='monthlyexam',
            field=models.PositiveIntegerField(default=0, verbose_name='考试编号'),
        ),
        migrations.AlterField(
            model_name='finalexam',
            name='finalexamnum',
            field=models.PositiveIntegerField(default=0, verbose_name='考试编号'),
        ),
    ]
