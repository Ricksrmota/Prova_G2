# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-20 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatoVaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoEleicao', models.CharField(max_length=5)),
                ('dataInicio', models.DateField(blank=True, null=True)),
                ('dataFim', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eleitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('cpf', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoToken', models.CharField(max_length=5)),
                ('voltou', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Urna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codUrna', models.CharField(max_length=5)),
                ('codigoCandidato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao.CandidatoVaga')),
                ('codigoEleicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao.Eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoVaga', models.CharField(max_length=5)),
                ('vaga', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('eleitor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eleicao.Eleitor')),
                ('codigoCandidato', models.CharField(max_length=5)),
            ],
            bases=('eleicao.eleitor',),
        ),
        migrations.AddField(
            model_name='token',
            name='cpf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicao.Eleitor'),
        ),
        migrations.AddField(
            model_name='eleicao',
            name='codigoVaga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao.Vaga'),
        ),
        migrations.AddField(
            model_name='candidatovaga',
            name='codigoVaga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao.Vaga'),
        ),
        migrations.AddField(
            model_name='candidatovaga',
            name='codigoCandidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eleicao.Candidato'),
        ),
    ]
