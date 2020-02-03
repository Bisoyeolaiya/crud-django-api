# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-27 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0002_auto_20191127_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(verbose_name='Task End Date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_startdate',
            field=models.DateField(verbose_name='Task Start Date'),
        ),
    ]