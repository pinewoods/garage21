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
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sensor_reading', models.IntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='WaterTank',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('device_key', models.CharField(max_length=32, unique=True, blank=True, editable=False)),
                ('total_height', models.FloatField()),
                ('air_gap', models.FloatField()),
                ('description', models.CharField(max_length=140, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reading',
            name='water_tank',
            field=models.ForeignKey(to='water_meter.WaterTank'),
        ),
    ]
