# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 00:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eleicao', '0008_auto_20171120_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatovaga',
            name='codigoCandidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidatovaga_candidato', to='eleicao.Candidato'),
        ),
        migrations.AlterField(
            model_name='urna',
            name='codigoCandidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vagaaa_candidato', to='eleicao.CandidatoVaga'),
        ),
    ]
