# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 02:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_auto_20170714_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bairro',
            field=models.CharField(blank=True, max_length=150, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='cep',
            field=models.CharField(blank=True, help_text='CEP 8 digitos (sem traços)', max_length=8, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='cidade',
            field=models.CharField(blank=True, max_length=100, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='complemento',
            field=models.CharField(blank=True, max_length=254, verbose_name='Complemento'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='logradouro',
            field=models.CharField(blank=True, max_length=254, verbose_name='Logradouro'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='numero_endereco',
            field=models.CharField(blank=True, max_length=254, verbose_name='Nº'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(verbose_name='date joined'),
        ),
    ]