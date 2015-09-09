# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='FeePrices',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('price_m3', models.FloatField(max_length=64)),
                ('band', models.FloatField(max_length=64)),
                ('consumer_type', models.ForeignKey(to='sabesp.ConsumerType')),
            ],
        ),
        migrations.CreateModel(
            name='HidrometroSabesp',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SabespProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('rgi', models.FloatField()),
                ('customer_id', models.FloatField()),
                ('supply_unit', models.CharField(blank=True, max_length=140)),
                ('consumption_goal', models.FloatField()),
                ('consumer_type', models.ForeignKey(to='sabesp.ConsumerType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SabespReading',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('reading_m3', models.FloatField(max_length=64)),
                ('reading_competence', models.DateField()),
                ('sabesp_profile', models.ForeignKey(to='sabesp.SabespProfile')),
                ('sensor_id', models.ForeignKey(to='sabesp.HidrometroSabesp')),
            ],
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, unique=True)),
                ('rate', models.FloatField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('consumer_type', models.ForeignKey(to='sabesp.ConsumerType')),
            ],
        ),
        migrations.AddField(
            model_name='hidrometrosabesp',
            name='sabesp_profile',
            field=models.ForeignKey(to='sabesp.SabespProfile'),
        ),
    ]
