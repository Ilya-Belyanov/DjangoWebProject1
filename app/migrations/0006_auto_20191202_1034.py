# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-02 07:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191130_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 2, 10, 34, 0, 567776), verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='data',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 2, 10, 34, 0, 568773), verbose_name='Дата'),
        ),
    ]
