# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 23:07
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('linkey', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='link',
            managers=[
                ('with_votes', django.db.models.manager.Manager()),
            ],
        ),
    ]
