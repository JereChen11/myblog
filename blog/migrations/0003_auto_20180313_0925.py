# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-13 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='auther',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='auther',
            new_name='author',
        ),
    ]
