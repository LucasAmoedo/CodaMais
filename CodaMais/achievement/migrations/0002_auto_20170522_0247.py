# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 05:47
from __future__ import unicode_literals

from django.db import migrations


def load_achievements_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "achievement")


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_achievements_from_fixture),
    ]
