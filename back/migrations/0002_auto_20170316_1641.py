# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ar_body',
            field=models.TextField(verbose_name='文章主要内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='ar_desc',
            field=models.CharField(max_length=255, verbose_name='文章描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='ar_name',
            field=models.CharField(max_length=30, verbose_name='文章名'),
        ),
        migrations.AlterField(
            model_name='article',
            name='timestamp',
            field=models.DateTimeField(verbose_name='文章建立时间'),
        ),
    ]