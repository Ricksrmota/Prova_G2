# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleicao', '0006_auto_20171120_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urna',
            old_name='codigoVaga',
            new_name='codigoCandidato',
        ),
    ]
