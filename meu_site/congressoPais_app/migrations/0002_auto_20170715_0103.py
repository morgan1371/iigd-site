# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congressoPais_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Criancas',
            new_name='Crianca',
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='descreva',
            field=models.CharField(blank=True, max_length=254, verbose_name='Resposta'),
        ),
    ]
