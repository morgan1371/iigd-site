# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0007_customuser_congressopais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(null=True, verbose_name='date joined'),
        ),
    ]
