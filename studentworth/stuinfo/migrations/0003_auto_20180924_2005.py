# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-24 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuinfo', '0002_auto_20180924_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudentname',
            name='sudent_age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
        migrations.AddField(
            model_name='sudentname',
            name='sudent_gender',
            field=models.CharField(default=0, max_length=4, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='sudentname',
            name='sudent_phonenum',
            field=models.BigIntegerField(default=0, verbose_name='手机号码'),
        ),
        migrations.AddField(
            model_name='sudentname',
            name='sudent_schoolid',
            field=models.PositiveIntegerField(default=0, verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='sudentname',
            name='sudent_name',
            field=models.CharField(default=0, max_length=50, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='sudentname',
            name='sudent_name_new',
            field=models.CharField(default=0, max_length=50, verbose_name='新增姓名'),
        ),
    ]
