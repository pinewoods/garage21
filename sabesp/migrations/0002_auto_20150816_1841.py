# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sabesp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeePrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('price_m3', models.FloatField(max_length=64)),
                ('band', models.FloatField(max_length=64)),
                ('consumer_type', models.ForeignKey(to='sabesp.ConsumerType')),
            ],
        ),
        migrations.CreateModel(
            name='Taxe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('code', models.CharField(max_length=64, unique=True)),
                ('rate', models.FloatField(max_length=64)),
                ('description', models.CharField(max_length=256, blank=True)),
                ('consumer_type', models.ForeignKey(to='sabesp.ConsumerType')),
            ],
        ),
        migrations.RemoveField(
            model_name='feeprices',
            name='consumer_type',
        ),
        migrations.RemoveField(
            model_name='taxes',
            name='consumer_type',
        ),
        migrations.DeleteModel(
            name='FeePrices',
        ),
        migrations.DeleteModel(
            name='Taxes',
        ),
    ]
