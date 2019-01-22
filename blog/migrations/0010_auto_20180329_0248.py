# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 02:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20180328_0241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={},
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]